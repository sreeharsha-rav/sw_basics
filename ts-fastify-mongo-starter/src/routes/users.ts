import { FastifyInstance, FastifyRequest, FastifyReply } from 'fastify';
import { User } from '../types/user';

let users: User[] = [];
let nextId = 1;

export default async function (fastify: FastifyInstance) {
    // Get all users
    fastify.get('/', async (request: FastifyRequest, reply: FastifyReply) => {
        return users;
    });

    // Get a single user
    fastify.get('/:id', async (request: FastifyRequest<{ Params: { id: string } }>, reply: FastifyReply) => {
        const id = parseInt(request.params.id, 10);
        const user = users.find(u => u.id === id);
        if (!user) {
            reply.code(404).send({ error: 'User not found' });
        }
        return user;
    });

    // Create a new user
    fastify.post('/', async (request: FastifyRequest<{ Body: Omit<User, 'id'> }>, reply: FastifyReply) => {
        const { name, email } = request.body;
        const newUser: User = { id: nextId++, name, email };
        users.push(newUser);
        reply.code(201).send(newUser);
    });

    // Update a user
    fastify.put('/:id', async (request: FastifyRequest<{ Params: { id: string }, Body: Omit<User, 'id'> }>, reply: FastifyReply) => {
        const id = parseInt(request.params.id, 10);
        const { name, email } = request.body;
        const userIndex = users.findIndex(u => u.id === id);
        if (userIndex === -1) {
            reply.code(404).send({ error: 'User not found' });
        } else {
            users[userIndex] = { ...users[userIndex], name, email };
            return users[userIndex];
        }
    });

    // Delete a user
    fastify.delete('/:id', async (request: FastifyRequest<{ Params: { id: string } }>, reply: FastifyReply) => {
        const id = parseInt(request.params.id, 10);
        const userIndex = users.findIndex(u => u.id === id);
        if (userIndex === -1) {
            reply.code(404).send({ error: 'User not found' });
        } else {
            const deletedUser = users.splice(userIndex, 1)[0];
            return { message: 'User deleted', user: deletedUser };
        }
    });
}
