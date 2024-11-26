Cav API Rewrite using FASTapi and sqlmodel 

### Goals of this project:
- Drop in replacement for existing api
  - no changes to existing routes or data returns
  - utilize existing api keys
  - require zero dev work for existing api connections
- Allow for implementing new endpoints without disturbing existing workflows
- Be fast enough for cav use
- Be simple enough to allow future maintenance/extensibility without requiring extensive codebase knowledge