from flask import Flask, Blueprint, request, render_template, session, redirect

classes = Blueprint('classes', __name__, template_folder='templates')

@classes.route('/interactive-classes', methods=['GET'])
def interactive_classes():
    if session:
        return render_template('interactive_classes.html')
    else:
        return redirect('/login')
    
@classes.route('/interactive-classes/<class_name>', methods=['GET'])
def interactive_class(class_name):
    if session:
        return render_template('interactive_class.html', class_name=class_name)
    else:
        return redirect('/login')