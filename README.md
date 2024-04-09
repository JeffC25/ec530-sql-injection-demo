# SQL Injection Demo

This is an project has been created as an in-class exercise for the EC530 course in the department of Electrical and Computer Engineering at Boston University. The excercise can be accessed [here](https://sql-demo.yerf.dev/).

#### Disclaimer
This web application has been intentionally designed with vulnerabilities to SQL injection for educational purposes only. It is intended to be used as a demonstration tool to understand the risks and potential consequences associated with SQL injection attacks.

#### Important Points to Note:

- Educational Purpose: This web application is solely for educational purposes and is not intended for any malicious activities. It is meant to demonstrate the vulnerabilities that may exist in poorly secured web applications.

- Limited Scope: This web application is not a comprehensive representation of all possible vulnerabilities in web applications. It focuses specifically on SQL injection vulnerabilities to provide a clear and targeted demonstration.

- Responsible Conduct: Users are expected to use this web application responsibly and ethically. Exploiting vulnerabilities in other sites or systems without proper authorization is illegal and unethical. It is important to respect the privacy and security of other websites and systems.

- Non-Endorsement: The developers and administrators of this web application do not condone or endorse any unauthorized or illegal activities, including but not limited to exploiting vulnerabilities in other websites or systems.

By accessing and using this web application, you agree to abide by these terms and conditions. The developers and administrators of this web application are not liable for any misuse or unauthorized activities performed by users.

## Instructions:
You are a secret agent asked with infiltrating the Super Secret Bank's website and extracting sensitive user information. This financial institution is rumored to be harboring valuable data on its high-profile clients, which could be leveraged for our organization's benefit.

Thanks to the efforts of your agency colleagues, we've gained valuable intel on how the website operates. The table of interest in the database has the following fields:
`id, username, name, birthday, secret, occupation, email, address, favorite_color, total_tacos_eaten`
Moreover, the website's backend only executes a single query per request, and responds with only the first result found.

Your task is to inspect the HTML and JavaScript code of the website and identify opportunities for exploitation. Utilize your skills to modify the client-side code in order to craft SQL injection attacks that will allow you to retrieve the following information:

- The name of user sportyjoe22
- The name of the user with an id of 44
- The name of the oldest user
- The name of the user who owns a pet fish
- The name of the user who works as a super villain
- The name of the oldest user born before 1985
- The names of the 2 users who secretly owns a secret lab
- The names of the 3 users whose favorite color is Yellow
- The names of the 4 users who are confirmed to have siblings
- The name of user who has the 5th highest number of tacos consumed
- The name of the user who secretly possessed a waterlife-related superpower and whose favorite color is Blue
