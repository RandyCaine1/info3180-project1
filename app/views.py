"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, datetime, random, re, uuid
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required
from models import UserProfile
from werkzeug.utils import secure_filename
from form import ProfileForm

###
# Routing for your application.
###


@app.route('/profile', methods=['POST','GET'])
def profile():
    form = ProfileForm()
        
    if request.method == 'POST':
        if form.validate_on_submit():

            # collection of data from the form
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            gender = form.gender.data
            location = form.location.data
            bio = form.bio.data
            dateCreated = datetime.date.today()
            
            photo = form.photo.data
            
            photo = request.files['photo']
            
            imagename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))
            
            user = UserProfile(firstname=firstname, lastname=lastname,email=email,gender=gender,bio=bio, photo=imagename, created_on=dateCreated, location=location)
                
            db.session.add(user)
            db.session.commit()
                
            flash("Profile Successfully Created", "success")
            return redirect(url_for("profiles"))
    
    
    
    return render_template('addprofile.html', form=form)


@app.route('/profiles',methods=['POST','GET'])
def profiles():
    all_profile = UserProfile.query.all()
    return render_template("profiles.html", Profile_users=all_profile)
    
@app.route('/profiles/<userid>', methods=['POST', 'GET'])
def profileView(userid):
    user = UserProfile.query.filter_by(userid=userid).first()
    if user is not None:
        return render_template('profile.html',user=user)
    else:
        flash('Unable to view user profile', 'danger')
        return redirect(url_for('profile'))    
    
def AllowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']    


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
