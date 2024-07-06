import { FastifyInstance } from 'fastify';
import { buildApp } from '../app';
import prisma from '../db';
import { User } from '../types/user';

describe('User API', () => {
    let app: FastifyInstance;

    beforeAll(async () => {
        app = buildApp();
        await app.ready();

        // clear the database
        await prisma.user.deleteMany();
    });

    afterAll(async () => {
        await prisma.user.deleteMany();
        await prisma.$disconnect();
        await app.close();
    });

    /* TEST CASES */

    // Create a new user and check ID type
    it('should create a new user and return a numeric ID', async () => {
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
        expect(typeof user.id).toBe('number'); // Ensure ID is a number
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

    // TODO: Get a single user using the numeric ID from created user


    // TODO: Update a user using the numeric ID from created user


    // TODO: Delete a user using the numeric ID from created user

});