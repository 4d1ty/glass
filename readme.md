# Glass

A simple multiplayer game.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/4d1ty/glass.git
    cd glass
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r req.txt
   ```
3. Set environment variables:
   ```bash
   #.env file
   SECRET_KEY=[YOUR SECRET KEY]
   ```
   **TIP:** generate a secret key using Python:
   
   ```
   python -c 'import secrets; print(secrets.token_hex())'
   ```

4. Run the game:
   ```bash
   flask --app server.py run # --debug [for debug mode]
   ```