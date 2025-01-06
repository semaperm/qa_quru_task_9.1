from selene import browser, by, have
from data_sources import resources
from data_sources.user_data import User


class PracticeFormPage:

    def open_browser(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def register_user(self, value: User):
        browser.element('[id="firstName"]').type(value.first_name),
        browser.element('[id="lastName"]').type(value.last_name)
        browser.element('[id="userEmail"]').type(value.email)
        browser.element(by.text(value.gender)).click()
        browser.element('[id="userNumber"]').type(value.user_number)
        browser.element("#subjectsInput").type(value.subject).press_enter()
        browser.element("#dateOfBirthInput").click()
        browser.element("[class='react-datepicker__year-select']").click().element(
            by.text(f"{value.birthday_date.get("year")}")).click()
        browser.element("[class='react-datepicker__month-select']").click().element(
            by.text(f"{value.birthday_date.get("month")}")).click()
        browser.element(by.text(f"{value.birthday_date.get("day")}")).click()
        if value.hobbies.get("Sports") is True:
            browser.element(by.text("Sports")).click()
        if value.hobbies.get("Music") is True:
            browser.element(by.text("Music")).click()
        if value.hobbies.get("Reading") is True:
            browser.element(by.text("Reading")).click()

        browser.element('#uploadPicture').set_value(resources.path(value.file))
        browser.element('[id="state"]').click()
        browser.element(by.text(value.state)).click()
        browser.element('[id="city"]').click()
        browser.element(by.text(value.city)).click()
        browser.element('[id="currentAddress"]').type(value.address)
        browser.element('[id="submit"]').click()

    def should_registered_user_with(self, user: User):
        full_name = user.first_name + " " + user.last_name
        email = user.email
        gender = user.gender
        user_number = user.user_number
        birthdate = user.birthday_date.get("day") + " " + user.birthday_date.get(
            "month") + "," + user.birthday_date.get("year")
        subjects = user.subject
        checked_hobby = [key for key, value in user.hobbies.items() if value is True]
        hobby = ", ".join(checked_hobby)
        file = user.file
        address = user.address
        location = user.state + " " + user.city
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                user_number,
                birthdate,
                subjects,
                hobby,
                file,
                address,
                location,
            )
        )