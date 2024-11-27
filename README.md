# FAST cavAPI

---

## Cav API Rewrite using FastAPI and SQLModel

### Project Goals:
- **Drop-in replacement** for the existing API:
  - No changes to existing routes or data returns.
  - Utilize the current API keys.
  - Require zero development effort for existing API connections.
- Enable **easy addition of new endpoints** without disrupting existing workflows.
- Ensure performance is **optimized for Cav use**.
- Keep the architecture **simple** for future maintenance and extensibility, minimizing the need for extensive knowledge of the codebase or libraries.

---

## Project File Structure

FAST cavAPI is structured into several folders, each serving a specific purpose. Below is an overview of the folder structure and its contents:

```
/app
    ├── main.py           # The entry point of the application
    ├── /api              # Contains route handlers (API endpoints). These are versioned.
    ├── /core             # Configuration, database session setup, and utilities
    ├── /models           # SQLAlchemy table models
    ├── /services         # Business logic and SQL lookups
    └── /schemas          # Pydantic models used for data validation and response serialization
```
