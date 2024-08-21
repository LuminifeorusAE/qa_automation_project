import allure

from pages.form_page import FormPage


@allure.suite('Test Form')
class TestForm:
    @allure.feature('Test form page')
    class TestFormPage:
        @allure.title('Check test form')
        def test_form(self, driver):
            """
            Test case to fill and verify the test form on the automation practice form page.

            Steps:
            1. Navigate to the form page.
            2. Fill in the form fields with data.
            3. Retrieve the result after form submission.

            Asserts:
            - The first name, last name, and email are correctly submitted in the form.
            """
            # Initialize the FormPage object with the specified URL
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()

            # Fill in the form fields and store the returned personal information
            p = form_page.fill_form_fields()

            # Retrieve the result of the form submission
            result = form_page.form_result()

            # Assert that the first name, last name, and email match the expected results
            assert [p.first_name + " " + p.last_name, p.email] == result[:2], "The form has not been filled"
