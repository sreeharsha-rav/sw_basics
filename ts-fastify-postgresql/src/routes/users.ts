import { FastifyInstance, FastifyRequest, FastifyReply } from 'fastify';
import prisma from '../db';
import { User } from '../types/user';

export default async function (fastify: FastifyInstance) {
    // Get all users
    fastify.get('/', async (request: FastifyRequest, reply: FastifyReply) => {
        return prisma.user.findMany();
    });

    // Get a single user
    fastify.get('/:id', async (request: FastifyRequest<{ Params: { id: number } }>, reply: FastifyReply) => {
        const { id } = request.params;

        const user = await prisma.user.findUnique({ where: { id } });
        if (!user) {
            reply.code(404).send({ error: 'User not found' });
        }
        return user;
    });

    // Create a new user
    fastify.post('/', async (request: FastifyRequest<{ Body: Omit<User, 'id'> }>, reply: FastifyReply) => {
        const { name, email } = request.body;
        const newUser = await prisma.user.create({
            data: { name, email }
        });
        reply.code(201).send(newUser);
    });

    // Update a user
    fastify.put('/:id', async (request: FastifyRequest<{ Params: { id: number }, Body: Omit<User, 'id'> }>, reply: FastifyReply) => {
        const { id } = request.params;
        const { name, email } = request.body;
        try {
            const updatedUser = await prisma.user.update({
                where: { id },
                data: { name, email }
            });
            return updatedUser;
        } catch (error) {
            reply.code(404).send({ error: 'User not found' });
        }
    });

    // Delete a user
    fastify.delete('/:id', async (request: FastifyRequest<{ Params: { id: number } }>, reply: FastifyReply) => {
        const { id } = request.params;
        try {
            const deletedUser = await prisma.user.delete({
                where: { id }
            });
            return { message: 'User deleted', user: deletedUser };
        } catch (error) {
            reply.code(404).send({ error: 'User not found' });
        }
    });
}
