#!/bin/env python
import os
from app import create_app, socketio, ROOMS

app = create_app(debug=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='0.0.0.0', port=port)

