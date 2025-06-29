import streamlit as st
import pandas as pd

from filter_engine import apply_standard_filters, apply_custom_filter
from template_engine import render_template
from template_manager import (
    load_templates,
    add_or_update_template,
    delete_template,
)
from rag_module import get_rag_answer
from evaluation import similarity
from test_manager import add_test


def main():
    st.title("Dynamic DataFrame Query Assistant")

    uploaded = st.file_uploader("Upload CSV or Excel")
    if uploaded:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
        st.write("Data Loaded", df.head())

        filters = {}
        for col in df.columns:
            if st.checkbox(f"Filter by {col}"):
                if pd.api.types.is_numeric_dtype(df[col]):
                    low = st.number_input(f"{col} min", value=float(df[col].min()))
                    high = st.number_input(f"{col} max", value=float(df[col].max()))
                    filters[col] = (low, high)
                else:
                    value = st.text_input(f"{col} value")
                    if value:
                        filters[col] = value

        if st.text_area("Custom Filter Function", key="custom_func"):
            code = st.session_state["custom_func"]
            try:
                # dangerously evaluate user code in a local scope
                local_vars = {}
                exec(code, {}, local_vars)
                func = local_vars.get("filter_func")
                if func:
                    df_filtered = apply_custom_filter(df, func)
                else:
                    st.error("Define a function named filter_func")
                    return
            except Exception as exc:
                st.error(f"Custom filter error: {exc}")
                return
        else:
            df_filtered = apply_standard_filters(df, filters)

        st.subheader("Query Result")
        st.write(df_filtered)

        # Template management
        templates = load_templates()
        template_names = list(templates.keys())
        new_option = "<New Template>"
        selected = st.selectbox("Choose Template", template_names + [new_option])
        if selected != new_option:
            template_name = selected
            template_content = templates[selected]
        else:
            template_name = st.text_input("Template Name")
            template_content = ""

        template = st.text_area("Message Template", template_content, key="tmpl")

        col_save, col_delete = st.columns(2)
        if col_save.button("Save Template"):
            if template_name:
                add_or_update_template(template_name, template)
                st.success("Template saved")
            else:
                st.error("Template name required")

        if selected != new_option and col_delete.button("Delete Template"):
            delete_template(template_name)
            st.success("Template deleted")

        if st.button("Generate Answer"):
            context = {
                "count": len(df_filtered),
                "rows": df_filtered.to_dict(orient="records"),
                "result": df_filtered,
            }
            answer = render_template(template, context)
            st.write("Answer:", answer)

            question = st.text_input("Question", "")
            rag_answer = get_rag_answer(question)
            st.write("RAG Answer:", rag_answer)
            score = similarity(answer, rag_answer)
            st.write(f"Similarity: {score:.2f}")

            if st.button("Save as Test Case"):
                add_test({"question": question, "filters": filters, "template": template, "expected": answer})
                st.success("Test case saved")


if __name__ == "__main__":
    main()
