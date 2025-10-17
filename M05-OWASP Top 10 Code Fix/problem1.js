// vurnability Broken Access Control
// issue req.params.userId is sent by the user and is being passed in

app.get('/profile/:userId', (req, res) => {
    User.findById(req.params.userId, (err, user) => {
        if (err) return res.status(500).send(err);
        res.json(user);
    });
});

// fixed version
// finds the user by an token tied to the profile completly bypassing user input

app.get('/profile', authenticateToken, async (req, res) => {
  try {
    const user = await User.findById(req.user.id); 
    if (!user) return res.status(404).send('User not found');
    res.json(user);
  } catch (err) {
    res.status(500).send(err.message);
  }
});