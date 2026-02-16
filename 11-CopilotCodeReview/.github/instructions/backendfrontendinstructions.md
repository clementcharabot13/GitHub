---
applyTo: "backend/**/*,*.py"
---

## Backend Guidelines

- All API endpoints must be defined in the `routers` folder.
- Load example database content from the `database.py` file.
- Error handling is only logged on the server. Do not propagate to the frontend.
- Ensure all APIs are explained in the documentation.
- Verify changes in the backend are reflected in the frontend (`src/static/**`). If possible breaking changes are found, mention them to the developer.
---
applyTo: "*.html,*.css,*.js"
---

## Frontend Guidelines

- Use accessibility attributes (alt text, aria labels) and color schemes.
- Use responsive design for compatibility with mobile devices.
- Validate HTML structure and semantic elements
