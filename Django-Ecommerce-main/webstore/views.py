from django.templatetags.static import static
from django.shortcuts import get_object_or_404, render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User, Category, Product
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date
form_path = 'C:\\Users\\Admin\\OneDrive\\Desktop\\Automatic filling - Copy\\Automatic_filling.pdf'
pdfmetrics.registerFont(TTFont('Calibri', 'Calibri.ttf'))
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))


# Views for the app webstore here.

def index(request):
    return render(request, "home.html")

# def login_user(request):
    
#     if request.method == "POST":
#         def my_view(request):
#             username = request.POST["username"]
#             email = request.POST["email"]
#             password = request.POST["password"]
#             user = authenticate(request, username=username,email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("home")
#             # Redirect to a success page.

#             else:
#                 return redirect("login")
# # Return an 'invalid login' error message.


#     else:
#         return render(request, "login.html")

def contact(request):
    return render(request, "contact.html")

def admission(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        contact_info = request.POST.get('contact_info')
        address = request.POST.get('address')
        coach = request.POST.get('coach')
        branch = request.POST.get('branch')
        parent_name = request.POST.get('parent_name')
        parent_profession = request.POST.get('parent_profession')
        parent_relation = request.POST.get('parent_relation')
        Relation = request.POST.get('Relation')

        # Create a new user
        new_user = User.objects.create_user(
            username = str(first_name) + " " + str(last_name),
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            contact_info = contact_info,
            address = address,
            # Add more user fields as needed
        )

        # Generate PDF report
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'contact_info': contact_info,
            'address': address,
            'branch': branch,
            'coach' : coach,
            'parent_name': parent_name,
            'parent_profession': parent_profession,
            'parent_relation': parent_relation,
            'Relation': Relation

            # Add more data as necessary
        }

        # Render admission successful pdf page
        pdf_response = generate_pdf_report(user_data)
        return pdf_response
    return render(request, "admission.html")

def store(request):
    context = {
        "products": Product.objects.all(),
        "categories": Category.objects.all()
    }
    return render(request, "store.html",context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)

def purchase(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    context = {
        'product': product,
        'user': user
    }
    return render(request, 'purchase.html', context)

def confirm_purchase(request, product_id):
    if request.method == 'POST':
        # Assuming you have a model named PurchaseDetails to store purchase information
        # Retrieve form data and save it to the database
        name = request.POST.get('name')
        address = request.POST.get('address')
        payment_info = request.POST.get('payment')

        # Save purchase details to the database (replace this with your model and save logic)
        # purchase = PurchaseDetails(name=name, address=address, payment_info=payment_info, ...)
        # purchase.save()

        # Fetch the product based on the product_id (for displaying the product details in the confirmation)
        product = get_object_or_404(Product, pk=product_id)

        # Pass the product and purchase details to the confirmation template
        context = {
            'product': product,
            'name': name,
            'address': address,
            'payment_info': payment_info,
            # Add more data as needed
        }

        return render(request, 'confirm_purchase.html', context)

    # Handle if the request method is not POST (if needed)
    # For example, redirecting to the product detail page or any other view
    return render(request, 'some_other_page.html')

def generate_pdf_report(user_data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="admission_report.pdf"'
    today = date.today().strftime("%Y-%m-%d")
    # Create a canvas
    p = canvas.Canvas(response, pagesize=letter)

    # Set up text content in the PDF
    # Add more fields as necessary
    
    image_path = 'Django-Ecommerce-main/webstore/static/img/GTA.jpg'
    img = ImageReader(image_path)
    p.drawImage(img, 500, 710, width=80, height=80)
    # p.drawImage('GTA.jpg',500,710,width=80, height=80)

    p.setFont("Calibri",22)
    p.setFillColorRGB(2,0,0)
    p.drawString(100,730,"Gurukul Taekwondo Acadamy")

    p.setStrokeColor('black')
    p.setLineWidth(2)
    p.line(10,700,600,700)

    p.setStrokeColor('black')
    p.setLineWidth(2)
    p.line(10,650,600,650)

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(20, 610, "Branch:")

    p.setLineWidth(1)
    p.line(65,608,180,608)

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(70, 610, f'{user_data.get("branch")}')

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(300, 610, "Date of Admission:")

    p.setLineWidth(1)
    p.line(410,608,560,608)

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(415, 610, f'{today}')

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(20, 570, "Name of Coach:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(120, 570, f'{user_data.get("coach")}')

    p.setFont("Calibri", 24)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(250, 520, "Student Form")


    p.setLineWidth(1)
    p.line(248,518,388,518)

    p.setLineWidth(1)
    p.line(115,568,560,568)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(20, 480,"New Admission")
    p.roundRect(110,473,20,20,2,stroke=1)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(250, 480,"Re-Admission")
    p.roundRect(335,473,20,20,2,stroke=1)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(460, 480,"Renewal Form")
    p.roundRect(550,473,20,20,2,stroke=1)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(20, 435,"Name of the Student:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(160, 435, f'{user_data.get("first_name")} {user_data.get("last_name")}')

    p.setLineWidth(1)
    p.line(150,432,470,432)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(20, 410,"Date of Birth:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(110, 410, f'{user_data.get("date_of_birth")}')

    p.setLineWidth(1)
    p.line(100,408,300,408)

    p.drawString(305, 410,"(Adhar Card Copy required)")

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(20, 385,"Address:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(80, 385, f'{user_data.get("address")}')

    p.setLineWidth(1)
    p.line(75,383,470,383)

    p.setLineWidth(1)
    p.line(20,358,470,358)

    p.setLineWidth(1)
    p.roundRect(480, 340, 90, 120, 3, stroke=1, fill=0)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(20,325,"Contact-Number:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(120, 325, f'{user_data.get("contact_info")}')

    p.setLineWidth(1)
    p.line(120,323,300,323)

    p.setFont("Calibri", 24)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(250, 290, "In case of minor")

    p.setLineWidth(1)
    p.line(248,288,388,288)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(20, 260,"Name of the Parent:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(160, 260, f'{user_data.get("parent_name")}')

    p.setLineWidth(1)
    p.line(150,258,470,258)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(20, 235,"Relation:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(80, 235, f'{user_data.get("Relation")}')

    p.setLineWidth(1)
    p.line(80,233,250,233)

    p.setFont("Calibri",14)
    p.setFillColorRGB(0,0,0)
    p.drawString(260, 235,"Profession:")

    p.setFont("Calibri", 14)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(330, 235, f'{user_data.get("parent_relation")}')

    p.setLineWidth(1)
    p.line(330,233,470,233)

    p.setLineWidth(1)
    p.roundRect(480, 160, 90, 120, 3, stroke=1, fill=0)


    p.setLineWidth(2)
    p.roundRect(10, 10, 590, 770, 8, stroke=1, fill=0)

    p.showPage()
    p.save()
    return response