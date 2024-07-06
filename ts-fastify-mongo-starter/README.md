# Fastify TypeScript Starter

A simple REST API for managing users, built with Fastify and TypeScript.

## Project Structure

```
project-root/
├── src/
│   ├── index.ts
│   ├── app.ts
│   ├── routes/
│   │   └── users.ts
│   ├── types/
│   │   └── user.ts
│   └── tests/
│       └── users.test.ts
├── Dockerfile
├── .dockerignore
├── .gitignore
|── api_endpoints.json
├── package.json
├── pnpm-lock.yaml
├── tsconfig.json
├── jest.config.js
└── nodemon.json
```

## Data Model

### User

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}
```

## API Endpoints

| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| GET    | /api/users     | Get all users           |
| GET    | /api/users/:id | Get a single user by ID |
| POST   | /api/users     | Create a new user       |
| PUT    | /api/users/:id | Update a user by ID     |
| DELETE | /api/users/:id | Delete a user by ID     |

## Setup and Running

1. Install dependencies:
   ```
   pnpm install
   ```

2. Run in development mode:
   ```
   pnpm dev
   ```

3. Build for production:
   ```
   pnpm build
   ```

4. Run in production mode:
   ```
   pnpm start
   ```

5. Run tests:
   ```
    pnpm test
   ```

## Docker

Build the Docker image:
```
docker build -t fastify-ts-user-api .
```

Run the Docker container:
```
docker run -p 8080:8080 fastify-ts-user-api
```

## API Usage Examples

For detailed examples of how to use the API with curl commands, please refer to the endpoints in [api_endpoints.json](./api_endpoints.json).