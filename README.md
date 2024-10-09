# Flask Bear Selector

This is a simple Flask web application that allows users to choose their favorite bear from a selection on the homepage. The app demonstrates the use of URL routing, templates, static files, and URL redirection. It also handles 404 errors and displays a custom error page.

## Features

- **Home Page**: Displays a form where users can select their favorite bear.
- **About Page**: Describes more information about bears.
- **Result Page**: Displays the user's selected bear after submitting the form.
- **404 Error Handling**: Displays a custom error page when an invalid URL is accessed.

## File Structure

- `app.py`: The main Python file containing the Flask routes and application logic.
- `templates/`: Contains all HTML files used by the Flask app.
  - `home.html`: Homepage with bear selection form.
  - `about.html`: About page with bear information.
  - `result.html`: Displays the selected bear.
  - `error.html`: Custom error page for handling 404 errors.
- `static/`: Contains static files such as CSS and images.

## Installation

1. **Clone the repository**

2. **Install Dependencies"":

   pip install flask

3. **Run the Application**:

   python app.py
