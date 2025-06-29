# Product Requirements Document (PRD)

## Project: Dynamic DataFrame Query Assistant with RAG Evaluation

### Overview
This tool provides a GUI (built with Streamlit) to query uploaded CSV or Excel
files via standard or custom pandas filters. The query results are rendered
through user-defined templates and compared with Retrieval Augmented Generation
(RAG) answers. Users can manage templates and test cases directly from the UI.
The code base is modular to encourage customization and extension.

### Functional Requirements
1. **Data Input**
   - Upload CSV or Excel files to create pandas DataFrames.
   - Support multiple filters on columns and optional custom filter functions.
   - Allow execution of DataFrame code snippets in a controlled environment.

2. **Answer Generation**
   - Render answers using message templates with variables from pandas queries.
   - Templates handle scalars and lists via Jinja2 style syntax.

3. **RAG Comparison**
   - Generate alternative answers via a RAG module.
   - Display similarity metrics between DataFrame answers and RAG answers.

4. **Template Management**
   - Create, edit, and delete templates in the GUI.
   - Templates persist to a JSON file for reuse.

5. **Test Case Generation & Management**
   - After evaluation, a **Save as Test Case** button stores the question,
     filter configuration or custom code, template, and resulting answer.
   - Test cases can be duplicated from the UI for similar questions.
   - A dedicated tab lists all test cases allowing view, edit, and delete.
   - Test cases are stored in a structured JSON file for version control.

### Non-Functional Requirements
- **Usability:** The GUI should be intuitive with clear labels and tooltips.
- **Extensibility & Modularity:** Separate modules for data handling,
  filtering, templating, and UI allow easy customization.
- **Performance:** Operations on DataFrames up to 1GB should remain responsive
  with progress indicators for long tasks.
- **Security:** Code execution must be sandboxed (e.g., via Docker) to protect
  the host environment.
- **Statefulness:** The application retains state during a user session
  including loaded data, filters, and custom code.

### Future Enhancements
- Export evaluation reports.
- Multi-language template support.
- Integration with version control for templates and tests.
