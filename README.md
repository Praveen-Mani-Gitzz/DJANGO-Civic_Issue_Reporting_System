
🏙️ CiviConnect – Civic Issue Reporting System

CiviConnect is a web-based civic issue reporting platform built using Django.
It enables citizens to report local public issues and allows municipal officers (admins) to track, manage, and resolve those issues efficiently through a centralized system.

The project focuses on **transparency, accountability, and structured communication** between the public and authorities.

📌 Project Objective

The main objective of CiviConnect is to simplify the process of reporting civic problems and ensure users can track the progress of their complaints.
Instead of manual follow-ups or unstructured communication, this system provides a digital workflow with status updates, attachments, and admin responses.

👤 User Capabilities

A registered user can:

* Create an account and log in securely
* Submit new civic complaints with:

  * Title
  * Description
  * Category (Road, Water, Garbage, etc.)
  * Address
  * Priority level
  * Optional contact details
* Upload **multiple photos or videos** as proof of the issue
* View all submitted complaints under **My Complaints**
* Track complaint status:

  * Pending
  * In Progress
  * Resolved
  * Delayed
* View replies from municipal officers
* See admin-uploaded images/videos showing work progress

Unauthorized users:

* Can only view the home page
* Must register or log in to submit or view complaints

🛠️ Admin / Officer Capabilities

Admins (municipal officers) can:

* Access a secure admin dashboard
* View all complaints submitted by users
* Search and filter complaints by:

  * Status
  * Category
  * Priority
  * User
* Update complaint status
* Add official replies to complaints
* Upload images/videos as proof of work completion
* Review user-uploaded attachments directly in the admin panel
* Maintain a complete history of complaint communication

🧩 Major Features Implemented

* User Authentication & Authorization
* Role-based access (User vs Admin)
* CRUD operations for complaints
* Multiple file upload support
* Admin replies with attachments
* Status-based complaint tracking
* Secure access control using decorators
* Clean and responsive UI
* Media handling for images and videos
* Django Admin customization

🏗️ Project Architecture

Frontend (UI)

* HTML templates using Django Template Language (DTL)
* Inline CSS for clean and consistent UI
* Responsive layout for desktop and mobile

Backend

* Django framework
* Function-based views
* Django ORM for database operations

Database

* SQLite (default Django database)
* Used for development and testing
* Can be replaced with MySQL or PostgreSQL for production

Media Handling

* `FileField` for storing images and videos
* Media served via Django settings in development

Admin Panel

* Django Admin interface
* Inline models for attachments and replies
* Custom list views and filters

🧪 Technologies Used

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **SQLite**
* **Django ORM**
* **Django Admin**

📂 Project Structure (Simplified)

```
CiviConnect/
│
├── citygram/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│
├── templates/
│   ├── citygram/
│   │   └── home.html
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   ├── complaint_form.html
│   └── my_complaints.html
│
├── media/
│   ├── attachments/
│   └── reply_attachments/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

🔐 Access Control Logic

* Home page is public
* Registration and Login required to:

  * Submit complaints
  * View complaints
* Admin-only features protected using:

  * `@staff_member_required`
* User-specific complaints filtered using logged-in user context

🚀 Future Enhancements

* Email or SMS notifications on status change
* REST API integration
* Pagination for complaints
* Advanced analytics dashboard
* Role-based officer assignments
* Deployment with MySQL/PostgreSQL
* Cloud storage for media files

📄 Conclusion

CiviConnect demonstrates a complete Django-based project with real-world use cases.
It showcases backend logic, authentication, file handling, admin control, and user interaction in a structured and scalable manner.
* Live project explanation script

Just tell.
