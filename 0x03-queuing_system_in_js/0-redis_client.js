import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected');
});
client.on('error', (error) => {
  console.error(`Redis not connected: ${error}`);
}); 
