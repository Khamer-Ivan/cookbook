# Cookbook App

This Django application allows you to manage recipes and track the usage of ingredients.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Khamer-Ivan/cookbook.git
   
2. Navigate to the project directory:

    ```bash 
   cd your-cookbook-app

3. Create a virtual environment:

    ```bash
   python -m venv venv

4. Activate the virtual environment:

    On Windows:
    ```venv\Scripts\activate```

    On macOS/Linux:
   ```source venv/bin/activate```

5. Install dependencies:

    ```bash
   pip install -r requirements.txt


6. Apply migrations:

    ```bash
   python manage.py migrate

7. Run the development server:

    ```bash
   python manage.py runserver

The application will be available at http://127.0.0.1:8000/ by default.

## Usage
Navigate to the Cook Recipe page.

Select a recipe from the dropdown.

Click the "Cook Recipe" button to increment the count of cooked dishes for each ingredient in the selected recipe.
Contributing

Feel free to contribute to the development of this Cookbook App. You can submit issues or pull requests.