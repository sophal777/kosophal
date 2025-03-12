const express = require('express');
const { OAuth2Client } = require('google-auth-library');
const app = express();
const client = new OAuth2Client('1068349103755-7927uao4h897ujil3sqs5ah0pqkbcm6j.apps.googleusercontent.com');

// Middleware to parse JSON request bodies
app.use(express.json());

// Route for the root URL
app.get('/', (req, res) => {
    res.send('Welcome to the server!');
});

// API to verify the token
app.post('/verify-token', async (req, res) => {
    const { id_token } = req.body;

    try {
        // Verify the token
        const ticket = await client.verifyIdToken({
            idToken: id_token,
            audience: '1068349103755-7927uao4h897ujil3sqs5ah0pqkbcm6j.apps.googleusercontent.com', // Google Client ID
        });

        // Get user information from the payload
        const payload = ticket.getPayload();
        console.log('Verified User:', payload);

        // Respond with the user data (or store it in the session/database)
        res.json({
            message: 'User authenticated successfully',
            user: payload,
        });
    } catch (error) {
        res.status(401).json({ message: 'Invalid token', error: error.message });
    }
});

// Starting the server on port 3002
app.listen(3002, () => {
    console.log('Server is running on http://localhost:3002');
});