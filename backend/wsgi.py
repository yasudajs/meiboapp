import os
from app import create_app, db
from app.models import User, Contact, Group

# Flask アプリケーションの設定
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Contact': Contact, 'Group': Group}

if __name__ == '__main__':
    app.run(debug=True)