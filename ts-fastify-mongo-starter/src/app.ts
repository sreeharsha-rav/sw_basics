import Fastify, { FastifyInstance } from 'fastify';
import userRoutes from './routes/users';

export function buildApp(): FastifyInstance {
  const app: FastifyInstance = Fastify({
    logger: true
  });

  app.register(userRoutes, { prefix: '/api/users' });

  return app;
}