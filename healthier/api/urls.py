from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/$', views.UserDetail.as_view()),
    url(r'^consumer/get/$', views.ConsumerDetail.as_view()),
    url(r'^provider/get/$', views.ProviderDetail.as_view()),
    url(r'^docs/$', views.SwaggerSchemaView.as_view()),
]



""""

<div class="row">
                        	<div class="col-sm-12">
                        		<div class="card-box">

                        			<h4 class="header-title m-t-0 m-b-30">Edit your account details</h4>

                        			<div class="row">
                        				<div class="col-lg-12">
                        					<form class="form-horizontal" role="form" method="POST">
                                                                          {% csrf_token %}
                                                 <div class="form-group">
	                                                <label class="col-md-2 control-label">{{ form.username.label }}</label>
	                                                <div class="col-md-10">
	                                                    <input type="text" id="{{ form.username.html_name }}" name="{{ form.username.html_name }}" class="form-control" placeholder="{{ user.username }}">
	                                                </div>
	                                            </div>
                                                <div class="form-group">
	                                                <label class="col-md-2 control-label">{{ form.address.label }}</label>
	                                                <div class="col-md-10">
	                                                    <input type="text" id="{{ form.address.html_name }}" name="{{ form.address.html_name }}" class="form-control" placeholder="{{ user.country }}">
	                                                </div>
	                                            </div>
                                                <input type="hidden" id="email" value="{{ user.email }}">
                                                <div class="form-group">
	                                                <label class="col-md-2 control-label">{{ form.country.label }}</label>
	                                                <div class="col-md-10">
	                                                    <input type="text" id="{{ form.country.html_name }}" name="{{ form.country.html_name }}" class="form-control" placeholder="{{ user.country }}">
	                                                </div>
	                                            </div>
                                                <div class="form-group">
	                                                <label class="col-md-2 control-label">{{ form.city.label }}</label>
	                                                <div class="col-md-10">
	                                                    <input type="text" id="{{ form.city.html_name }}" name="{{ form.city.html_name }}" class="form-control" placeholder="{{ user.city }}">
	                                                </div>
	                                            </div>
                                                <div class="form-group">
	                                                <label class="col-md-2 control-label">{{ form.phone_number.label }}</label>
	                                                <div class="col-md-10">
	                                                    <input type="text" id="{{ form.phone_number.html_name }}" class="form-control" name="{{ form.phone_number.html_name }}" placeholder="{{ user.phone_number }}">
	                                                </div>
	                                            </div>
                                                <div class="form-group">
	                                                <label class="col-md-2 control-label">{{ form.description.label }}</label>
	                                                <div class="col-md-10">
	                                                    <textarea rows="7" id="{{ form.description.html_name }}" name="{{ form.description.html_name }}" class="form-control" placeholder="{{ user.description }}"></textarea>
	                                                </div>
	                                            </div>
                                                <div class="form-group">
	                                                <label class="col-md-2 control-label">{{ form.website.label }}</label>
	                                                <div class="col-md-10">
	                                                    <input class="form-control" id="{{ form.website.html_name }}" name="{{ form.website.html_name }}" placeholder="{{ user.website }}"/>
	                                                </div>
	                                            </div>
                                                    <button type="button" id="updateAccountDetailsBtn" class="btn btn-lg btn-googleplus waves-effect waves-light">Submit</button>
	                                        </form>
                        				</div>
                        			</div><!-- end row -->
                        				"""