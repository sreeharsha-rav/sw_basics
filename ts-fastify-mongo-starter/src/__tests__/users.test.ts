import { FastifyInstance } from 'fastify';
import { buildApp } from '../app';
import { User } from '../types/user';

describe('User API', () => {
    let app: FastifyInstance;

    beforeAll(async () => {
        app = buildApp();
        await app.ready();
    });

    afterAll(async () => {
        await app.close();
    });

    /* TEST CASES */

    // Create a new user
    it('should create a new user', async () => {
        const response = await app.inject({
            method: 'POST',
            url: '/api/users',
            payload: {
                name: 'John Doe',
                email: 'john@example.com'
            }
        });

        expect(response.statusCode).toBe(201);
        const user: User = JSON.parse(response.payload);
        expect(user).toHaveProperty('id');
        expect(user.name).toBe('John Doe');
        expect(user.email).toBe('john@example.com');
    });

    // Get all users
    it('should get all users', async () => {
        const response = await app.inject({
            method: 'GET',
            url: '/api/users'
        });

        expect(response.statusCode).toBe(200);
        const users: User[] = JSON.parse(response.payload);
        expect(Array.isArray(users)).toBe(true);
    });

    // Get a single user
    it('should get a single user', async () => {
        // Create a user first
        const createResponse = await app.inject({
            method: 'POST',
            url: '/api/users',
            payload: {
                name: 'Jane Doe',
                email: 'jane@example.com'
            }
        });
        const createdUser: User = JSON.parse(createResponse.payload);

        const response = await app.inject({
            method: 'GET',
            url: `/api/users/${createdUser.id}`
        });

        expect(response.statusCode).toBe(200);
        const user: User = JSON.parse(response.payload);
        expect(user).toEqual(createdUser);
    });

    // Update a user
    it('should update a user', async () => {
        // Create a user first
        const createResponse = await app.inject({
            method: 'POST',
            url: '/api/users',
            payload: {
                name: 'Bob Smith',
                email: 'bob@example.com'
            }
        });
        const createdUser: User = JSON.parse(createResponse.payload);

        const response = await app.inject({
            method: 'PUT',
            url: `/api/users/${createdUser.id}`,
            payload: {
                name: 'Robert Smith',
                email: 'robert@example.com'
            }
        });

        expect(response.statusCode).toBe(200);
        const updatedUser: User = JSON.parse(response.payload);
        expect(updatedUser.id).toBe(createdUser.id);
        expect(updatedUser.name).toBe('Robert Smith');
        expect(updatedUser.email).toBe('robert@example.com');
    });

    // Delete a user
    it('should delete a user', async () => {
        // Create a user first
        const createResponse = await app.inject({
            method: 'POST',
            url: '/api/users',
            payload: {
                name: 'Alice Johnson',
                email: 'alice@example.com'
            }
        });
        const createdUser: User = JSON.parse(createResponse.payload);

        const response = await app.inject({
            method: 'DELETE',
            url: `/api/users/${createdUser.id}`
        });

        expect(response.statusCode).toBe(200);
        const result = JSON.parse(response.payload);
        expect(result.message).toBe('User deleted');
        expect(result.user).toEqual(createdUser);
    });
});
