import subprocess, os
import re
import wget as wg
opa_pc=0

def cmdo(com):
	try:
		res=subprocess.check_output(com, shell=1)
	except:
		return '🖥❌'
	try:
		res=res.decode('utf8')
	except:
		try:
			res=res.decode('cp866')
		except:
			return '🖥❌'
	return '🖥✅:\n'+res


def cmdi(com):
	try:
		os.system(com)
		return '🖥✅'
	except:
		return '🖥❌'

def wget(link,save):
	try:
		wg.download(link, save)
		return '🖥✅'
	except: return '🖥❌🗡'
def comm(text):
	comi4=re.findall(r'<([^<>]+)>', text)
	try:
		return comi4, True
	except:
		return None, False

def com_bot(kl):
	res='Нет такой команды, зато есть такие:\n\nСписок функций и их использование:\n1. Выполнить команду, на её вывод всё-равно:    cmdi: <команда>\n2. Выполнить команду и вернуть её вывод в телеграмм: cmdo: <команда>\n3. Сохранить фото, аудио или видео на ПК:    просто отправить этот файл\n4. Скачать файл из интернета:    wget <ссылка>\n\nКоманты и ссылки обязателно надо писать в <>'
	try:
		inp,i=comm(kl)
		print(inp)
		if kl.lower()[:4]=='cmdi' and i:
			res=cmdi(inp[0])
		elif kl.lower()[:4]=='cmdo' and i:
			res=cmdo(inp[0])
		elif kl.lower()[:4]=='wget' and i:
			res=wget(inp[0],inp[1])
		return res


	except: return res
# print(com_bot(input()))
# print(cmdo("dir"))