from flask import Blueprint, render_template, redirect
from flask_login import current_user, login_required
from ..models import Package, db
from ..forms.shipping_form import ShippingForm

bp = Blueprint('routes', __name__)


@bp.route('/')
@login_required
def index():
    packages = Package.query.filter(Package.user_id == current_user.id).all()
    return render_template('package_status.html', packages=packages)


@bp.route('/new_package', methods=["GET", "POST"])
@login_required
def new_package():
    form =ShippingForm()

    if form.validate_on_submit():
        data = form.data
        sender = f'{current_user.first_name} {current_user.last_name}'
        new_package = Package(sender=sender,
                              recipient=data["recipient"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"],
                              user=current_user)
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')

    return render_template('shipping_request.html', form=form)
