# What I Learnt In This Project

# Edit a  Profile:
1:Display the Form to Edit the Profile:
  in forms.py define you form:

  class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email")
        widgets = {
                'username': forms.TextInput(attrs={
                    'class': 'mt-1 ml-2 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                    'placeholder': 'Enter your username',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                    'placeholder': 'Enter your email',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateUser, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'email']:
                self.fields[fieldname].help_text = None

    class UpdateProfile(forms.ModelForm):
        
        class Meta:
            model = ProfileUser
            fields = ("image",)
        widgets = {
                'image': forms.ClearableFileInput(attrs={
                    'class': 'mx-auto mt-1 block w-full text-sm text-gray-500 rounded-md border border-gray-300 cursor-pointer focus:outline-none focus:ring-blue-500 focus:border-blue-500',
                }),
            }

2:Render Forms :
    def Profile_View(request):
    if request.method == "POST":
        u_form = UpdateUser(request.POST or None,instance=request.user)
        p_form = UpdateProfile(request.POST or None,request.FILES or None,instance = reques.user.profileuser)
    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profileuser)

    profile = Profile.objects.filter(user=request.user).first()
    context={
        'u_form':u_form,
        'profile':profile,
        'p_form':p_form
    }
    return render(request,'User/profile.html',context)

3: Render in Template:
   <div class="mb-4 flex space-x-8">
        {{ u_form.username.label_tag }}
        {{ u_form.username }}
        {% if u_form.username.errors %}
          <p class="text-sm text-red-600 mt-1">{{ u_form.username.errors|striptags }}</p>
        {% endif %}
    </div>

<h1>User Uploading Blog or Post</h1><br>
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    posts = PostModel.objects.all()  # Fetch all posts to display on the page
    

    if request.method == 'POST':
        post=PostModel.objects.all()#rendering all post from database
        form = PostModelForm(request.POST, request.FILES)  # Include request.FILES if handling file uploads
        if form.is_valid():
            instance = form.save(commit=False)  # Don't commit yet to assign the author
            instance.author = request.user  # Assign the currently logged-in user as the author
            instance.save()  # Save the post
            return redirect('index')  # Redirect to the index page after successful post creation
        else:
            form = PostModelForm()  # Instantiate an empty form for the initial GET request

    context = {
        'posts': posts,
        'form': form,
        'post':post
    }
    return render(request, 'index.html', context)


# Save Your App name Like This: 'appname.apps.AppnameConfig', instead of 'appname',


# To refer to a field of a Category model related to Product model by Foreinkey use this format <mode_lname>__<model_field>

as in: products = Product.objects.filter(category__slug="Fashion")

def collectionview(request,slug):
    if (Category.objects.filter(slug=slug,status=0)):
        product = Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first() 
                                                    #Only one object having this slig

# Get the newest product
newest_product = Product.objects.order_by('-created_at').first()

# JQuery 
CDN link on https://releases.jquery.com/ 
choose JQuery 3.X minified >> select the src https://code.jquery.com/jquery-3.7.1.min.js and browse it >> Paste the results in a file with js extension (in static folder)
include this js file in base.html

Now write JQuery in your code as per your need in a file custom.js

# add functionality to Increment and Decrement button
jqdoc{
    jqclick{
        let var = jqfind (fetch value)
        write the login to increase the value
    }
}
jqdoc{
    $('.increment_btn').on('click', function (e) {
       console.log("button clicked :D");
       e.preventDefault();

       // Find the closest product_val and decrement the qty-input value
       var inc_value = $(this).closest('.product_val').find('.qty_input').val();
       var value = parseInt(inc_value, 10);

       value = isNaN(value) ? 0 : value;  // Ensure value is a number
       if (value < 10) {  // Allow decrement until the value is 1
           value++;
           $(this).closest('.product_val').find('.qty_input').val(value);
       }
     });
}

# Alertufy JS
copy alertify js CDN
<!-- JavaScript -->
<script src="//cdn.jsdelivr.net/npm/alertifyjs@1.14.0/build/alertify.min.js"></script>
add this in base.html

link CSS
<!-- CSS -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.14.0/build/css/alertify.min.css"/>
<!-- Default theme -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.14.0/build/css/themes/default.min.css"/>
Navigate to Components >> Notifier >> Position >>
 <script>
 alertify.set('notifier','position', 'top-right');
  {% for msg in messages %} 
 alertify.success('{{msg}}');
 {%  endfor %}
 </script>

# To Prevent unauthorized access to certain page:
from django.contrib.auth.decorators import login_required
@login_required
in settings.py 
LOGIN_URL = 'login'

