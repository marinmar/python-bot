# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:19:34 2019

@author: marin
"""

from selenium import webdriver
import time
import datetime 

browser = webdriver.Firefox(executable_path=r'C:\Users\marin\Desktop\bot python\geckodriver.exe')
browser.get('https://web.whatsapp.com')

time.sleep(20)

index=0
Max=-9999

last_message=""

members=["Olivia","Cam Ly Rintz","Helene Marissal","Axelle Sander","Nathan Dermenjian","Aubin Lecoz","Emma Louise","Coraline Franceseti","marin"]

important=[]

polls=[]

#text_box = browser.find_element_by_xpath("//span[contains(@title, 'EL CHOCAMÁN')]")
#print(text_box.text)

    
def get_last_message(last_message):
    index=0
    Max=-9999
    try:
        text_box = browser.find_elements_by_class_name("FTBzM")
        for i in range(len(text_box)):
            if (text_box[i].location['y']>Max):
                index=i
                Max=text_box[i].location['y']
        if (text_box[index].text != last_message):
            return(text_box[index].text)
        else:
            return False
    except:
        return False

def commande(text,author):
    
    if text[0:8]=="!activer":
        print("ok")
        text_box = browser.find_element_by_class_name("_3u328")
        text_box.send_keys("successfully activated bot V1.1 For other commands see !help \n")
    if text[0:5]=="!help":
        text_box = browser.find_element_by_class_name("_3u328")
        text_box.send_keys("Bienvenue sur le nouveau bot chocaman ! Voici quelques commandes utiles: \n")
        time.sleep(2)
        text_box.send_keys("-> !important: Voici comment stocker les infos importantes du moment: taper important précédé d'un point d'exclamation, tapez votre texte puis ajouter un chiffre à la fin, un ou deux. Pour les afficher, tapez !important Le chiffre à la fin donne le délai d'expiration \n")
    if text[0:10]=="!important":
        com_important(text)
    if text[0:8]=="!sondage":
        sondage(text,author)
    if text[1:11]=="désactiver"and author=="marin":
        text_box = browser.find_element_by_class_name("_3u328")
        text_box.send_keys("Done ! Shutting down at "+str(datetime.datetime.now()) +"\n")
        quit()
        
        
def com_important(text): 
    global important
    now = datetime.datetime.now()
      
    if len(text)>10:
        try:
            if int(text[len(text)-1])==1:
                expire=now + datetime.timedelta(days=1)
            else:
                expire=datetime.datetime.now() + datetime.timedelta(days=7)
            important.append([text[11:len(text)-1],expire])
            text_box = browser.find_element_by_class_name("_3u328")
            text_box.send_keys("Done, expire le "+str(expire)+" \n")
        except:
            text_box = browser.find_element_by_class_name("_3u328")
            text_box.send_keys("erreur ! Avez vous pensé au délai ? \n")
    else:
        if len(important)!=0:
            text_box = browser.find_element_by_class_name("_3u328")
            text_box.send_keys("Infos importantes: \n") 
            time.sleep(1)
            j=0
            
            for i in range(len(important)):
                if(important[i-j][1]<now):
                    important.remove(important[i-j])
                    j+=1
            
            for i in range(len(important)):
                delta=important[i][1]-now
                if delta.days != 0:
                    t=str(delta.days)+" d"
                else:
                    t=str(delta.seconds//3600)+" h"
                text_box.send_keys(important[i][0]+"\n") 
                time.sleep(0.5)
        else:
            text_box = browser.find_element_by_class_name("_3u328")
            text_box.send_keys("Pas d'infos importantes ! \n") 
            time.sleep(0.5)

def sondage(text,author):
    text=text[9:]
    #text=text.split(",")
    for i in polls:
        if i[0] in text:
            try:
                k=int(text[len(text)-1])
                if k<=len(polls[i][2]):
                    add_vote(text,author,k)
                else:
                    text_box = browser.find_element_by_class_name("_3u328")
                    text_box.send_keys("erreur !\n")
                return()
            except:
                print_vote(text)
                return()
    add_sond(text)   
                
def add_vote(text,author,k):
    for i in range(len(polls)):
        if polls[i][0] in text:
            for j in range(len(members)):
                if members[j]==author:
                    polls[i][3][j]=k  
    
def print_vote(text):
    for i in range(len(polls)):
        if polls[i][0] in text:
            text_box = browser.find_element_by_class_name("_3u328")
            text_box.send_keys(polls[i][1]+": \n")
            time.sleep(1)
            for j in range(len(polls[i][3])):
                if polls[i][3][j]!=-1:
                    text_box.send_keys(members[j]+": "+polls[i][2][polls[i][3][j]-1]+" \n")
                    time.sleep(1)
            

def add_sond(text):
    text=text.split("(")
    text=text[1][:len(text[1])-1]
    text=text.split(",")
    new_poll = [text[0],text[1],text[2:],[-1 for i in range(len(members))] ]
    polls.append(new_poll)
    

while True:
    a=get_last_message(last_message)
    if a: 
        last_message=a
        a=a.splitlines()
        
        text=""
        timer=a[len(a)-1]
        text_list=a[:len(a)-1]
        
        
#        file2write=open("test.txt",'w')
#        file2write.write(author+"/"+text+"/"+timer+"\n")
#        file2write.close()
        
        author="marin"
        if len(text_list)==0:
            text_list=["null"]
        if text_list[0] in ["Olivia","Cam Ly Rintz","Helene Marissal","Axelle Sander","Nathan Dermenjian","Aubin Lecoz","Emma Louise","Coraline Franceseti"]:
            author=text_list[0]
            text_list=text_list[1:]
            if len(text_list)==0:
                text_list=["null"]
        text=text.join(text_list)
        print(author,text,timer)
        
        if text[0]=="!":
            commande(text,author)
    time.sleep(1)








#text_box.send_keys(response)


#    text_box = browser.find_element_by_class_name("_3u328")
#    now = datetime.datetime.now()
#    minute=int(now.minute)
#    hour=int(now.hour)
#    if minute == hour:
#        text_box.send_keys("Je bosse mon TD de physique !\n")
#        time.sleep(60)
        
    
    