kolichestvo_vypolnennyh_dz = '12'
kolichestvoZatrachennyhChasov = '1.5'
nazvanie_kursa = 'Python'
vremyaNaOdnoZadanie = str(float(kolichestvoZatrachennyhChasov) / int(kolichestvo_vypolnennyh_dz))
print("Курс" + ":" + ' ' + nazvanie_kursa + ',' + ' ' + 'всего задач' + ":" + kolichestvo_vypolnennyh_dz + ',' + ' ' + 'затрачено часов' + ': ' + kolichestvoZatrachennyhChasov + ', ' + 'среднее время выполнения' + ' ' + vremyaNaOdnoZadanie + ' ' + 'часа' + '.')