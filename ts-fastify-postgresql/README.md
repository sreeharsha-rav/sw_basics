# Fastify TypeScript Starter

A simple REST API for managing users, built with Fastify, TypeScript, Prisma and PostgreSQL.

## Technologies

- Fastify
- TypeScript
- Prisma
- PostgreSQL
- Jest

## Project Structure

```
project-root/
├── src/
│   ├── index.ts
│   ├── app.ts
│   ├── db.ts
│   ├── routes/
│   │   └── users.ts
│   ├── types/
│   │   └── user.ts
│   └── tests/
│       └── users.test.ts
├── prisma/
│   ├── schema.prisma
│   └── seed.ts
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

```prisma
model User {
  id    Int     @id @default(autoincrement())
  name  String
  email String  @unique
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

2. Set up your MongoDB database and update the `DATABASE_URL` in the `.env` file.

3. Run Prisma migrations:
   ```
   npx prisma db push
   ```

4. Seed the database with sample data:
   ```
   pnpm seed
   ```

5. Run in development mode:
   ```
   pnpm dev
   ```

6. Build for production:
   ```
   pnpm build
   ```

7. Run in production mode:
   ```
   pnpm start
   ```

8. Run tests:
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
docker run -p 3000:3000 -e DATABASE_URL=your_database_url fastify-ts-user-api
```

## API Usage Examples

For detailed examples of how to use the API with curl commands, please refer to the endpoints in [api_endpoints.json](./api_endpoints.json).

## Further Updates

- Tests for routes (GET :id, PUT, DELETE)
- Add authentication and authorization