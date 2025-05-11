
def main_func():
    import os
    from openai import OpenAI
    import json

    # Assuming your JSON is stored in a file named 'emails.json'r
    with open('mails.json', 'r', encoding='utf-8') as file:
        json_data = file.read()

    # Convert JSON to a Python list of dictionaries
    emails_list = json.loads(json_data)
    # for i in emails_list.values():
    #     print(i)
    vals = emails_list
    # print(vals['items'][0]['header'])
    string_val = ""
    #
    #  Now 'emails_list' is a Python list containing your email data
    n = 1
    for i in emails_list['items']:
        string_val += str(n) + "\"" + ' ' + "header: \n" + i['header'] + "Date: " + i['date'] + "content: " + i['content'] + "\"" + "\n"
        n = n + 1
    #
    catogories=["Project Updates", "Meeting Invitations", "Code Reviews", "Bug Reports and Issue Tracking",
                "Collaboration and Communication", "Policy and Process Updates", "Training and Development", "System Outages or Critical Alerts"
                "Release Notes", "Recruitment and Hiring", "Security Alerts"]
    cats = ""
    for i in catogories:
        cats = cats + i + ", "
    number_of_categories = len(catogories)
    request_text = "I will provide you with some mails, " \
                   "your task is to analyze all of it and find similarities. If you " \
                   "find similarities, like 2 emails in your opinion are on the same subject, " \
                   "then you need to create a category and list these emails under this category. So you should " \
                   "categorize it. For example, if some emails are on the same topic, let's say from Reddit, " \
                   "you create a category called \"Reddit\" and list it under this category. Create as few " \
                   "categories as possible, merge emails under a certain category." \
                   " Generalize categories and have more emails under one category." \
                   " You need to have as few categories as possible and have more emails under one category. " \
                   "YOU ARE ALLOWED TO HAVE ONLY " + str(number_of_categories) + " categories! AND YOU NEED TO use these categories: " + cats +  " Only if text is totally on different topic, you can create your own category, but try to used categories that I provided! " \
                                                                                                                                                 "Here is a list of the content of mails : \"" + string_val + "\". " \
                     "It is necessary so the output would be like: Category:, Header:, Date:, Content:"

    client = OpenAI(
        # This is the default and can be omitted
        api_key='ADD-YOUR-API-KEY, I RAN OUT OF MONEY :)',
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request_text,
            }
        ],
        model="gpt-3.5-turbo",
    )
    assistant_reply = chat_completion
    ob = assistant_reply.choices[0]
    CCM = ob.message
    return CCM.content
print(main_func())