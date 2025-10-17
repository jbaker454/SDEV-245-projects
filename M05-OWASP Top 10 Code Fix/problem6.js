// vurnability Injection
// issue req.query.username passed in directly

app.get('/user', (req, res) => {
    // Directly trusting query parameters can lead to NoSQL injection
    db.collection('users').findOne({ username: req.query.username }, (err, user) => {
        if (err) throw err;
        res.json(user);
    });
});

// fixed version
// similar to problem 1 get the user id from session instead thus eliminating the issue entirely

app.get('/user', authenticateToken, async (req, res) => {
  try {
    const user = await db.collection('users')
      .findOne({ _id: new ObjectId(req.user.id) }, { projection: { password: 0 } });
    if (!user) return res.status(404).json({ error: 'User not found' });
    res.json(user);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server error' });
  }
});