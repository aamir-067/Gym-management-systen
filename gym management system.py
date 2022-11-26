from tkinter import *
class customers:
    def __init__(self,cost_id,name,adress,contact,email) -> None:
        self.cost_id= cost_id
        self.name=name
        self.adress=adress
        self.contact=contact
        self.email=email
class trainer:
    def __init__(self,trainer_id,name) -> None:
        self.trainer_id = trainer_id
        self.name=name
class plan:
    def __init__(self,plan_id,trainer_id,equipment_id,duration) -> None:
        self.plan_id=plan_id
        self.trainer_id=trainer_id
        self.equipment_id=equipment_id
        self.duration=duration
class equipment:
    def __init__(self,e_id,e_name) -> None:
        self.e_id = e_id
        self.e_name = e_name
class subscription:
    def __init__(self,sub_id,date,cost_id,trainer_id,exe_id):
        self.sub_id = sub_id
        self.date = date
        self.cost_id = cost_id
        self.trainer_id = trainer_id
        self.exe_id = exe_id

# default costumers .. which we added 
costumers={}    # dictionary which will save all objects of costumers
costumers[f'costumer_{1}']=customers(1,'Aamir Khan','Surrani Bannu','+92 3441259408','aamirkhan@engineer.com')
costumers[f'costumer_{2}']=customers(2,'Tawab Sarhadi','Surrani Bannu kpk','+92 3359585423','tawabsarhadi95@gmail.com')
costumers[f'costumer_{3}']=customers(3,'Ahmad Khan','kotaka khatakan surrani','+92 3319293226','ahmadzajorryu@gmail.com')
# default trainers .... which i added.
trainers={} # dictionary of trainers
trainers[f'trainer_{1}'] = trainer(1,'Hassan rafay')
trainers[f'trainer_{2}'] = trainer(2,'Siham ullah shah')
trainers[f'trainer_{3}'] = trainer(3,'Hamza siddique')
# default plans i added 
plans={}
plans[f'plan_{1}'] = plan(1,2,2,'30min')
plans[f'plan_{2}'] = plan(2,3,1,'20min')
plans[f'plan_{3}'] = plan(3,3,2,'15min')
# default equipments i added 
equipments={}
equipments[f'equipment_{1}']=equipment(1,'sqaut machine')
equipments[f'equipment_{2}']=equipment(2,'Leg press machine')
equipments[f'equipment_{3}']=equipment(3,'cable cross')
# default subscriptions i added
subscriptions = {f'subscription_{1}': subscription(1,'28/8/2003',2,1,3),
                f'subscription_{2}':  subscription(2,'6/9/2022',3,1,1),
                f'subscription_{3}': subscription(3,'1/1/2022',2,2,1)
                }

# main window and tilte and logo
window = Tk()
window.title("GYM MANAGMENT SYSTEM")
window.iconbitmap('D:\\vs codes\\2nd semester\\for end semester project\\project\\bb.ico')
window.maxsize(width=400,height=400)
window.minsize(width=400,height=400)
def home():
    def clear_home():
        welcome.destroy()
        btn_of_costemers.destroy()
        btn_of_trainers.destroy()
        btn_of_equipments.destroy()
        btn_of_memberships.destroy()
        btn_of_exit.destroy()
        btn_of_plans.destroy()
#=====================================================
# code for costumers
    def One():
        clear_home()
        def clear_one():
            cost_id_in_one_label.destroy()
            cost_id_in_one_entry.destroy()
            btn_show.destroy()
            btn_add.destroy()
            btn_bak.destroy()
            btn_exi.destroy()
        def back():
            clear_one()
            home()

        # customes page linking. 1a,1b,1c......
        def customer_data(index):
            clear_one()
            def clear_customer_data():
                cost_id.destroy()
                value_of_id.destroy()
                name.destroy()
                value_of_name.destroy()
                adress.destroy()
                value_of_adress.destroy()
                contact.destroy()
                value_of_contact.destroy()
                email.destroy()
                value_of_email.destroy()
                edit.destroy()
                delete.destroy()
                back.destroy()
                exit.destroy()
            def del_or_back(is_del):
                if is_del == True:
                    del costumers[f'costumer_{index}']
                clear_customer_data()
                One()
            if f'costumer_{index}' not in costumers.keys():
            # ===> this will not run code forward if entered id is not exist
                One()
            else:
                cost_id=Label(window,text='id : ',font=('sans serifs',14))
                cost_id.place(x=80,y=20)
                value_of_id=Label(window,text=costumers[f'costumer_{index}'].cost_id,font=('sans serifs',14))
                value_of_id.place(x=110,y=20)

                name=Label(window,text='name : ',font=('sans serifs',14))
                name.place(x=80,y=50)
                value_of_name=Label(window,text=costumers[f'costumer_{index}'].name,font=('sans serifs',14))
                value_of_name.place(x=140,y=50)

                adress=Label(window,text='adress : ',font=('sans serifs',14))
                adress.place(x=80,y=80)
                value_of_adress=Label(window,text=costumers[f'costumer_{index}'].adress,font=('sans serifs',14))
                value_of_adress.place(x=160,y=80)

                contact=Label(window,text='contact : ',font=('sans serifs',14))
                contact.place(x=80,y=110)
                value_of_contact=Label(window,text=costumers[f'costumer_{index}'].contact,font=('sans serifs',14))
                value_of_contact.place(x=160,y=110)

                email=Label(window,text='email : ',font=('sans serifs',14))
                email.place(x=80,y=140)
                value_of_email=Label(window,text=costumers[f'costumer_{index}'].email,font=('sans serifs',14))
                value_of_email.place(x=150,y=140)
                # buttons

                # function to edit a costumer data  ===>  to open 1aa
                def edit_costumer(costumer_id):
                    clear_customer_data()
                    def clear_edit_costumer():
                        label_of_id.destroy()
                        entry_of_id.destroy()
                        label_of_name.destroy()
                        entry_of_name.destroy()
                        label_of_adress.destroy()
                        entry_of_adress.destroy()
                        label_of_contact.destroy()
                        entry_of_contact.destroy()
                        label_of_email.destroy()
                        entry_of_email.destroy()
                        btn_of_save.destroy()
                        btn_of_back.destroy()
                        btn_of_quit.destroy()

                    label_of_id=Label(window,text="Id :",font=('sans serifs',14))
                    label_of_id.place(x=80,y=50)
                    entry_of_id=Entry(window,width=30)
                    entry_of_id.insert(0,costumers[f'costumer_{costumer_id}'].cost_id)
                    entry_of_id.place(x=125,y=55)
                    temp_for_cost_id = entry_of_id.get()

                    label_of_name=Label(window,text="Name :",font=('sans serifs',14))
                    label_of_name.place(x=80,y=80)
                    entry_of_name=Entry(window,width=30)
                    entry_of_name.insert(0,costumers[f'costumer_{costumer_id}'].name)
                    entry_of_name.place(x=150,y=85)

                    label_of_adress=Label(window,text="adress :",font=('sans serifs',14))
                    label_of_adress.place(x=80,y=110)
                    entry_of_adress=Entry(window,width=30)
                    entry_of_adress.insert(0,costumers[f'costumer_{costumer_id}'].adress)
                    entry_of_adress.place(x=155,y=115)

                    label_of_contact=Label(window,text="contact :",font=('sans serifs',14))
                    label_of_contact.place(x=80,y=140)
                    entry_of_contact=Entry(window,width=30)
                    entry_of_contact.insert(0,costumers[f'costumer_{costumer_id}'].contact)
                    entry_of_contact.place(x=155,y=145)

                    label_of_email=Label(window,text="email :",font=('sans serifs',14))
                    label_of_email.place(x=80,y=170)
                    entry_of_email=Entry(window,width=30)
                    entry_of_email.insert(0,costumers[f'costumer_{costumer_id}'].email)
                    entry_of_email.place(x=155,y=175)

                    # btns in 1aa
                    def save_and_back(temp):
                        if temp==1:   # which means we click on save btn else on back btn
                            del costumers[f'costumer_{costumer_id}']
                            costumers[f'costumer_{int(entry_of_id.get())}'] = customers(int(entry_of_id.get()),entry_of_name.get(),entry_of_adress.get(),entry_of_contact.get(),entry_of_email.get())
                        clear_edit_costumer()
                        customer_data(temp_for_cost_id)

                    btn_of_save=Button(window,text='Save',command=lambda: save_and_back(1))
                    btn_of_save.place(x=80,y=230)
                    btn_of_back=Button(window,text='back',command=lambda: save_and_back(0))
                    btn_of_back.place(x=200,y=230)
                    btn_of_quit=Button(window,text='quit',command=window.quit)
                    btn_of_quit.place(x=300,y=230)

                edit=Button(window,text='Edit',command=lambda : edit_costumer(index))
                edit.place(x=100,y=200)
                delete=Button(window,text='Delete',command=lambda: del_or_back(True))
                delete.place(x=200,y=200)
                back=Button(window,text='back',command=lambda: del_or_back(False))
                back.place(x=100,y=240)
                exit=Button(window,text='exit',command=window.quit)
                exit.place(x=200,y=240)

        cost_id_in_one_label = Label(window,text='Costumer Id : ',font=('sans-serifs',12))
        cost_id_in_one_label.place(x=50,y=50)
        cost_id_in_one_entry=Entry(window,width=20)
        cost_id_in_one_entry.place(x=150,y=55)

        # btns
        def One_d():
            clear_one()

            # function that works for add new costumer and back from one_d window to One.
            def back_and_add(add_var):
                if add_var==int(1):
                    costumers[f'costumer_{int(entry_of_id.get())}']=customers(int(entry_of_id.get()),entry_of_name.get(),entry_of_adress.get(),entry_of_contact.get(),entry_of_email.get())

                label_of_id.destroy()
                entry_of_id.destroy()
                label_of_name.destroy()
                entry_of_name.destroy()
                label_of_adress.destroy()
                entry_of_adress.destroy()
                label_of_contact.destroy()
                entry_of_contact.destroy()
                label_of_email.destroy()
                entry_of_email.destroy()
                btn_of_add.destroy()
                btn_of_back.destroy()
                btn_of_quit.destroy()
                One()

            label_of_id=Label(window,text="Id :",font=('sans serifs',14))
            label_of_id.place(x=80,y=50)
            entry_of_id=Entry(window,width=30)
            entry_of_id.place(x=125,y=55)
            label_of_name=Label(window,text="Name :",font=('sans serifs',14))
            label_of_name.place(x=80,y=80)
            entry_of_name=Entry(window,width=30)
            entry_of_name.place(x=150,y=85)
            label_of_adress=Label(window,text="adress :",font=('sans serifs',14))
            label_of_adress.place(x=80,y=110)
            entry_of_adress=Entry(window,width=30)
            entry_of_adress.place(x=155,y=115)
            label_of_contact=Label(window,text="contact :",font=('sans serifs',14))
            label_of_contact.place(x=80,y=140)
            entry_of_contact=Entry(window,width=30)
            entry_of_contact.place(x=155,y=145)
            label_of_email=Label(window,text="email :",font=('sans serifs',14))
            label_of_email.place(x=80,y=170)
            entry_of_email=Entry(window,width=30)
            entry_of_email.place(x=155,y=175)

            # btns in 1d
            btn_of_add=Button(window,text='add',command=lambda:back_and_add(1))
            btn_of_add.place(x=80,y=230)
            btn_of_back=Button(window,text='back',command=lambda:back_and_add(0))
            btn_of_back.place(x=200,y=230)
            btn_of_quit=Button(window,text='quit',command=window.quit)
            btn_of_quit.place(x=300,y=230)

        btn_show=Button(window,text='Show',command=lambda : customer_data(cost_id_in_one_entry.get()))
        btn_show.place(x=150,y=85)
        btn_add=Button(window,text='Add new',command=One_d)
        btn_add.place(x=150,y=120)
        btn_bak=Button(window,text='Back',command=back)
        btn_bak.place(x=150,y=150)
        btn_exi=Button(window,text='exit',command=window.quit)
        btn_exi.place(x=150,y=180)


    welcome=Label(window,text="WELCOME",font=("sans-serifs",25),fg="#000" , bg="#888")
    welcome.pack(fill=X)
    btn_of_costemers=Button(window,text="Costumers",command=One)
    btn_of_costemers.pack(pady=20,ipadx=5,ipady=5)
# ==================================================================
# code for trainers

    def two():
        clear_home()
        def clear_two():
            trainer_in_two_label.destroy()
            trainer_in_two_entry.destroy()
            btn_show.destroy()
            btn_add.destroy()
            btn_back.destroy()
            btn_exit.destroy()

        trainer_in_two_label = Label(window,text='Trainer Id : ',font=('sans-serifs',12))
        trainer_in_two_label.place(x=50,y=50)
        trainer_in_two_entry=Entry(window,width=20)
        trainer_in_two_entry.place(x=150,y=55)

        def two_a(trainer_id):        #function that show trainer
            clear_two()
            def clear_two_a():
                label_of_id.destroy()
                id_value.destroy()
                label_of_name.destroy()
                name_value.destroy()
                btn_edit.destroy()
                btn_del.destroy()
                btn_backkk.destroy()
                btn_quit.destroy()
            if f'trainer_{trainer_id}' not in trainers.keys():
                two()
            else:
                label_of_id=Label(window,text='Id : ',font=('sans serifs',14))
                label_of_id.place(x=70,y=50)
                id_value=Label(window,text=trainers[f'trainer_{trainer_id}'].trainer_id,font=('sans serifs',14))
                id_value.place(x=110,y=50)
                label_of_name=Label(window,text='Name : ',font=('sans serifs',14))
                label_of_name.place(x=70,y=100)
                name_value=Label(window,text=trainers[f'trainer_{trainer_id}'].name,font=('sans serifs',14))
                name_value.place(x=140,y=100)
            
                def edit_trainer(trainer_id):
                    clear_two_a()
                    id_label=Label(window,text='id :',font=('sans serifs',14))
                    id_label.place(x=50,y=50)
                    id_entery=Entry(window,width=30)
                    id_entery.place(x=100,y=55)
                    id_entery.insert(0,trainers[f'trainer_{trainer_id}'].trainer_id)
                    name_label=Label(window,text='Name :',font=('sans serifs',14))
                    name_label.place(x=50,y=100)
                    name_entery=Entry(window,width=30)
                    name_entery.place(x=135,y=105)
                    name_entery.insert(0,trainers[f'trainer_{trainer_id}'].name)

                    # btns
                    def save_n_back(is_save):   # if is_save==True then save changes else only back
                        if is_save == True:
                            del trainers[f'trainer_{trainer_id}']
                            trainers[f'trainer_{int(id_entery.get())}'] = trainer(int(id_entery.get()),name_entery.get())
                        id_label.destroy()
                        id_entery.destroy()
                        name_label.destroy()
                        name_entery.destroy()
                        back_btn.destroy()
                        save_btn.destroy()
                        quit_btn.destroy()
                        two_a(trainer_id)

                    back_btn=Button(window,text='Back',command=lambda : save_n_back(False))
                    back_btn.place(x=50,y=150)
                    save_btn=Button(window,text='Save',command=lambda : save_n_back(True))
                    save_btn.place(x=150,y=150)
                    quit_btn=Button(window,text='Quit',command=window.quit)
                    quit_btn.place(x=250,y=150)

                btn_edit=Button(window,text='Edit',command=lambda : edit_trainer(trainer_id))
                btn_edit.place(x=70,y=170)

                def backkk_or_del(is_del):
                    if is_del == True:
                        del trainers[f'trainer_{trainer_id}']
                    clear_two_a()
                    two()
                btn_del=Button(window,text='Delete',command=lambda: backkk_or_del(True))
                btn_del.place(x=170,y=170)
                btn_backkk=Button(window,text='Back',command=lambda:backkk_or_del(False))
                btn_backkk.place(x=70,y=220)
                btn_quit=Button(window,text='Quit',command=window.quit)
                btn_quit.place(x=170,y=220)

        btn_show=Button(window,text='Show',command=lambda: two_a(trainer_in_two_entry.get()))
        btn_show.place(x=150,y=85)

        def two_b():
            clear_two()
            id_label=Label(window,text='id :',font=('sans serifs',14))
            id_label.place(x=50,y=50)
            id_entery=Entry(window,width=30)
            id_entery.place(x=100,y=55)
            name_label=Label(window,text='Name :',font=('sans serifs',14))
            name_label.place(x=50,y=100)
            name_entery=Entry(window,width=30)
            name_entery.place(x=135,y=105)

            # btns
            def backk_and_save(is_save:bool):  # if is_save is True then it will save else only back
                if is_save == True:
                    trainers[f'trainer_{int(id_entery.get())}'] = trainer(int(id_entery.get()),name_entery.get())
                id_label.destroy()
                id_entery.destroy()
                name_label.destroy()
                name_entery.destroy()
                back_btn.destroy()
                save_btn.destroy()
                quit_btn.destroy()
                two()

            back_btn=Button(window,text='Back',command=lambda : backk_and_save(False))
            back_btn.place(x=50,y=150)
            save_btn=Button(window,text='Save',command=lambda : backk_and_save(True))
            save_btn.place(x=150,y=150)
            quit_btn=Button(window,text='Quit',command=window.quit)
            quit_btn.place(x=250,y=150)

        btn_add=Button(window,text='Add new',command=two_b)
        btn_add.place(x=150,y=120)

        def back():
            clear_two()
            home()
        btn_back=Button(window,text='Back',command=back)
        btn_back.place(x=150,y=150)
        btn_exit=Button(window,text='exit',command=window.quit)
        btn_exit.place(x=150,y=180)

    btn_of_trainers=Button(window,text="Trainers",command=two)
    btn_of_trainers.pack(ipadx=5,ipady=5)
# ====================================================================
# code for plans functionality
    def three():     # --> funtion which goto page three gets is and shows that id's plan
        clear_home()
        def clear_three():
            plan_in_three_label.destroy()
            plan_in_three_entry.destroy()
            btn_show.destroy()
            btn_addd.destroy()
            btn_back.destroy()
            btn_exit.destroy()
        plan_in_three_label = Label(window,text='Plan Id : ',font=('sans-serifs',12))
        plan_in_three_label.place(x=50,y=50)
        plan_in_three_entry=Entry(window,width=20)
        plan_in_three_entry.place(x=150,y=55)

        def show_plan(plan_id_para):  # ---> 3a
            clear_three()
            def clear_show_plan():
                back_btn.destroy()
                delete_btn.destroy()
                edit_btn.destroy()
                plan_id_label.destroy()
                trainer_id_label.destroy()
                equipment_id_label.destroy()
                duration_label.destroy()
                plan_id.destroy()
                trainer_id.destroy()
                equipment_id.destroy()
                duration.destroy()
            def back_and_del(is_back):
                if is_back == False:
                    del plans[f'plan_{plan_id_para}']
                clear_show_plan()
                three()

            if f'plan_{plan_id_para}' not in plans.keys():    #  ===> show plan if its exist else not gives response
                three()
            else:

                back_btn=Button(window,text="Back",command=lambda:back_and_del(True))
                back_btn.place(x=80,y=10)
                delete_btn=Button(window,text="Delete",command=lambda:back_and_del(False))
                delete_btn.place(x=190,y=10)

                def edit_plan(id_of_plan):
                    clear_show_plan()
                    plan_id_label_in_edit=Label(window,text="Plan Id :",font=('sans serifs',14))
                    plan_id_label_in_edit.place(x=80,y=50)
                    plan_id_entry_in_edit=Entry(window,width=20)
                    plan_id_entry_in_edit.place(x=160,y=55)
                    trainer_id_label_in_edit=Label(window,text="Trainer Id :",font=('sans serifs',14))
                    trainer_id_label_in_edit.place(x=80,y=80)
                    trainer_id_entry_in_edit=Entry(window,width=20)
                    trainer_id_entry_in_edit.place(x=180,y=85)
                    equipment_id_label_in_edit=Label(window,text="Equipment Id :",font=('sans serifs',14))
                    equipment_id_label_in_edit.place(x=80,y=110)
                    equipment_id_entry_in_edit=Entry(window,width=20)
                    equipment_id_entry_in_edit.place(x=210,y=115)
                    duration_label_in_edit=Label(window,text="Duration :",font=('sans serifs',14))
                    duration_label_in_edit.place(x=80,y=140)
                    duration_entry_in_edit=Entry(window,width=20)
                    duration_entry_in_edit.place(x=170,y=145)
                    # previos data insertion
                    plan_id_entry_in_edit.insert(0,plans[f'plan_{id_of_plan}'].plan_id)
                    trainer_id_entry_in_edit.insert(0,plans[f'plan_{id_of_plan}'].trainer_id)
                    equipment_id_entry_in_edit.insert(0,plans[f'plan_{id_of_plan}'].equipment_id)
                    duration_entry_in_edit.insert(0,plans[f'plan_{id_of_plan}'].duration)

                    # btns
                    def back_n_save(is_save):
                        if is_save ==True:
                            del plans[f'plan_{id_of_plan}']
                            plans[f'plan_{int(plan_id_entry_in_edit.get())}'] = plan(int(plan_id_entry_in_edit.get()),trainer_id_entry_in_edit.get(),equipment_id_entry_in_edit.get(),duration_entry_in_edit.get())
                        plan_id_label_in_edit.destroy()
                        plan_id_entry_in_edit.destroy()
                        trainer_id_label_in_edit.destroy()
                        trainer_id_entry_in_edit.destroy()
                        equipment_id_label_in_edit.destroy()
                        equipment_id_entry_in_edit.destroy()
                        duration_label_in_edit.destroy()
                        duration_entry_in_edit.destroy()
                        btn_of_back_in_edit.destroy()
                        btn_of_save_in_edit.destroy()
                        show_plan(id_of_plan)
                    btn_of_back_in_edit=Button(window,text='Back',padx=5,pady=5,command=lambda: back_n_save(False))
                    btn_of_back_in_edit.place(x=80,y=180)
                    btn_of_save_in_edit=Button(window,text='Save',padx=5,pady=5,command=lambda: back_n_save(True))
                    btn_of_save_in_edit.place(x=200,y=180)

                edit_btn=Button(window,text="edit",command=lambda : edit_plan(plan_id_para))
                edit_btn.place(x=300,y=10)
                # labels
                plan_id_label=Label(window,text="Plan id",font=('sans serifs',12))
                plan_id_label.place(x=30,y=50)
                trainer_id_label=Label(window,text="trainer id",font=('sans serifs',12))
                trainer_id_label.place(x=100,y=50)
                equipment_id_label=Label(window,text="equipment id",font=('sans serifs',12))
                equipment_id_label.place(x=180,y=50)
                duration_label=Label(window,text="duration",font=('sans serifs',12))
                duration_label.place(x=300,y=50)

                # values
                plan_id=Label(window,text=plans[f'plan_{plan_id_para}'].plan_id,font=('sans serifs',10))
                plan_id.place(x=30,y=80)
                trainer_id=Label(window,text=plans[f'plan_{plan_id_para}'].trainer_id,font=('sans serifs',10))
                trainer_id.place(x=100,y=80)
                equipment_id=Label(window,text=plans[f'plan_{plan_id_para}'].equipment_id,font=('sans serifs',10))
                equipment_id.place(x=180,y=80)
                duration=Label(window,text=plans[f'plan_{plan_id_para}'].duration,font=('sans serifs',10))
                duration.place(x=300,y=80)

        btn_show=Button(window,text='Show',command=lambda: show_plan(plan_in_three_entry.get()))
        btn_show.place(x=150,y=85)
        
        def add_plan():
            clear_three()

            plan_id_label=Label(window,text="Plan Id :",font=('sans serifs',14))
            plan_id_label.place(x=80,y=50)
            plan_id_entry=Entry(window,width=20)
            plan_id_entry.place(x=160,y=55)
            trainer_id_label=Label(window,text="Trainer Id :",font=('sans serifs',14))
            trainer_id_label.place(x=80,y=80)
            trainer_id_entry=Entry(window,width=20)
            trainer_id_entry.place(x=180,y=85)
            equipment_id_label=Label(window,text="Equipment Id :",font=('sans serifs',14))
            equipment_id_label.place(x=80,y=110)
            equipment_id_entry=Entry(window,width=20)
            equipment_id_entry.place(x=210,y=115)
            duration_label=Label(window,text="Duration :",font=('sans serifs',14))
            duration_label.place(x=80,y=140)
            duration_entry=Entry(window,width=20)
            duration_entry.place(x=170,y=145)
            # btns
            def back_n_save(is_save):
                if is_save ==True:
                    plans[f'plan_{int(plan_id_entry.get())}'] = plan(int(plan_id_entry.get()),trainer_id_entry.get(),equipment_id_entry.get(),duration_entry.get())
                plan_id_label.destroy()
                plan_id_entry.destroy()
                trainer_id_label.destroy()
                trainer_id_entry.destroy()
                equipment_id_label.destroy()
                equipment_id_entry.destroy()
                duration_label.destroy()
                duration_entry.destroy()
                btn_of_back.destroy()
                btn_of_save.destroy()
                three()

            btn_of_back=Button(window,text='Back',padx=5,pady=5,command=lambda: back_n_save(False))
            btn_of_back.place(x=80,y=180)
            btn_of_save=Button(window,text='Save',padx=5,pady=5,command=lambda: back_n_save(True))
            btn_of_save.place(x=200,y=180)

        btn_addd=Button(window,text='Add new',command=add_plan)
        btn_addd.place(x=150,y=120)
        def back():
            clear_three()
            home()
        btn_back=Button(window,text='Back',command=back)
        btn_back.place(x=150,y=150)
        btn_exit=Button(window,text='exit',command=window.quit)
        btn_exit.place(x=150,y=180)

    btn_of_plans=Button(window,text="Plans",command=three)
    btn_of_plans.pack(pady=20,ipadx=10,ipady=5)
# ===================================================================
# code for equipments
    def four():
        clear_home()
        def clear_four():
            equipment_in_four_label.destroy()
            equipment_in_four_entry.destroy()
            btn_show.destroy()
            btn_add.destroy()
            btn_back.destroy()
            btn_exit.destroy()
        equipment_in_four_label = Label(window,text='Equipment Id : ',font=('sans-serifs',12))
        equipment_in_four_label.place(x=50,y=50)
        equipment_in_four_entry=Entry(window,width=20)
        equipment_in_four_entry.place(x=170,y=55)

        def four_a(equipment_id):        #function that show trainer
            clear_four()
            def clear_four_a():
                label_of_id.destroy()
                id_value.destroy()
                label_of_name.destroy()
                name_value.destroy()
                btn_edit.destroy()
                btn_del.destroy()
                btn_backkk.destroy()
                btn_quit.destroy()
            if f'equipment_{equipment_id}' not in equipments.keys():
                four()
            else:
                label_of_id=Label(window,text='Id : ',font=('sans serifs',14))
                label_of_id.place(x=70,y=50)
                id_value=Label(window,text=equipments[f'equipment_{equipment_id}'].e_id,font=('sans serifs',14))
                id_value.place(x=110,y=50)

                label_of_name=Label(window,text='Name : ',font=('sans serifs',14))
                label_of_name.place(x=70,y=100)
                name_value=Label(window,text=equipments[f'equipment_{equipment_id}'].e_name,font=('sans serifs',14))
                name_value.place(x=140,y=100)
            
                def edit_equipment(equipment_id):
                    clear_four_a()
                    id_label=Label(window,text='id :',font=('sans serifs',14))
                    id_label.place(x=50,y=50)
                    id_entery=Entry(window,width=30)
                    id_entery.place(x=100,y=55)
                    id_entery.insert(0,equipments[f'equipment_{equipment_id}'].e_id)

                    name_label=Label(window,text='Name :',font=('sans serifs',14))
                    name_label.place(x=50,y=100)
                    name_entery=Entry(window,width=30)
                    name_entery.place(x=135,y=105)
                    name_entery.insert(0,equipments[f'equipment_{equipment_id}'].e_name)

                    # btns
                    def save_n_back(is_save):   # if is_save==True then save changes else only back
                        if is_save == True:
                            del equipments[f'equipment_{equipment_id}']
                            equipments[f'equipment_{int(id_entery.get())}'] = equipment(int(id_entery.get()),name_entery.get())
                        id_label.destroy()
                        id_entery.destroy()
                        name_label.destroy()
                        name_entery.destroy()
                        back_btn.destroy()
                        save_btn.destroy()
                        quit_btn.destroy()
                        four_a(equipment_id)

                    back_btn=Button(window,text='Back',command=lambda : save_n_back(False))
                    back_btn.place(x=50,y=150)
                    save_btn=Button(window,text='Save',command=lambda : save_n_back(True))
                    save_btn.place(x=150,y=150)
                    quit_btn=Button(window,text='Quit',command=window.quit)
                    quit_btn.place(x=250,y=150)

                btn_edit=Button(window,text='Edit',command=lambda : edit_equipment(equipment_id))
                btn_edit.place(x=70,y=170)

                def backkk_and_delete(is_del):
                    if is_del == True:
                        del equipments[f'equipment_{equipment_id}']
                    clear_four_a()
                    four()
                btn_del=Button(window,text='Delete',command=lambda: backkk_and_delete(True))
                btn_del.place(x=170,y=170)
                btn_backkk=Button(window,text='Back',command=lambda: backkk_and_delete(False))
                btn_backkk.place(x=70,y=220)
                btn_quit=Button(window,text='Quit',command=window.quit)
                btn_quit.place(x=170,y=220)
        
        btn_show=Button(window,text='Show',command=lambda: four_a(equipment_in_four_entry.get()))
        btn_show.place(x=150,y=85)

        def four_b():
            clear_four()

            id_label=Label(window,text='id :',font=('sans serifs',14))
            id_label.place(x=50,y=50)
            id_entery=Entry(window,width=30)
            id_entery.place(x=100,y=55)
            name_label=Label(window,text='Name :',font=('sans serifs',14))
            name_label.place(x=50,y=100)
            name_entery=Entry(window,width=30)
            name_entery.place(x=135,y=105)

            # btns
            def backk_and_save(is_save:bool):  # if is_save is True then it will save else only back
                if is_save == True:
                    equipments[f'equipment_{int(id_entery.get())}'] = equipment(int(id_entery.get()),name_entery.get())
                id_label.destroy()
                id_entery.destroy()
                name_label.destroy()
                name_entery.destroy()
                back_btn.destroy()
                save_btn.destroy()
                quit_btn.destroy()
                four()

            back_btn=Button(window,text='Back',command=lambda : backk_and_save(False))
            back_btn.place(x=50,y=150)
            save_btn=Button(window,text='Save',command=lambda : backk_and_save(True))
            save_btn.place(x=150,y=150)
            quit_btn=Button(window,text='Quit',command=window.quit)
            quit_btn.place(x=250,y=150)

        btn_add=Button(window,text='Add new',command=four_b)
        btn_add.place(x=150,y=120)

        def back():
            clear_four()
            home()
        btn_back=Button(window,text='Back',command=back)
        btn_back.place(x=150,y=150)
        btn_exit=Button(window,text='exit',command=window.quit)
        btn_exit.place(x=150,y=180)

    btn_of_equipments=Button(window,text="Equipments",command=four)
    btn_of_equipments.pack(ipadx=5,ipady=5)
# ===============================================================================================
# code for memberships
    def five():
        clear_home()
        def clear_five():
            sub_id_in_five_label.destroy()
            sub_id_in_five_entry.destroy()
            btn_show.destroy()
            btn_add.destroy()
            btn_back.destroy()
            btn_exit.destroy()
        sub_id_in_five_label = Label(window,text='Subscription Id : ',font=('sans-serifs',12))
        sub_id_in_five_label.place(x=50,y=50)
        sub_id_in_five_entry=Entry(window,width=20)
        sub_id_in_five_entry.place(x=170,y=55)
        def show_sub(sub_id):
            clear_five()
            def clear_show_sub():
                sub_id_label.destroy()
                sub_id_value.destroy()
                date_label.destroy()
                date_value.destroy()
                customer_id_label.destroy()
                customer_id_value.destroy()
                trainer_id_label.destroy()
                trainer_id_value.destroy()
                exersice_id_label.destroy()
                exersice_id_value.destroy()
                btn_of_back.destroy()
                btn_of_edit.destroy()
                btn_del.destroy()
            if f'subscription_{sub_id}' not in subscriptions.keys():
            # === > back to page five if sub_id is not in subscriptions
                five()
            else:
                sub_id_label=Label(window,text="sub Id :",font=('sans serifs',14))
                sub_id_label.place(x=80,y=50)
                sub_id_value=Label(window,text=subscriptions[f'subscription_{sub_id}'].sub_id,font=('sans serifs',14))
                sub_id_value.place(x=160,y=55)

                date_label=Label(window,text="date :",font=('sans serifs',14))
                date_label.place(x=80,y=80)
                date_value=Label(window,text=subscriptions[f'subscription_{sub_id}'].date,font=('sans serifs',14))
                date_value.place(x=160,y=85)

                customer_id_label=Label(window,text="customer Id :",font=('sans serifs',14))
                customer_id_label.place(x=80,y=110)
                customer_id_value=Label(window,text=subscriptions[f'subscription_{sub_id}'].cost_id,font=('sans serifs',14))
                customer_id_value.place(x=210,y=115)

                trainer_id_label=Label(window,text="trainer Id :",font=('sans serifs',14))
                trainer_id_label.place(x=80,y=140)
                trainer_id_value=Label(window,text=subscriptions[f'subscription_{sub_id}'].trainer_id,font=('sans serifs',14))
                trainer_id_value.place(x=180,y=145)

                exersice_id_label=Label(window,text="exersice id :",font=('sans serifs',14))
                exersice_id_label.place(x=80,y=170)
                exersice_id_value=Label(window,text=subscriptions[f'subscription_{sub_id}'].exe_id,font=('sans serifs',14))
                exersice_id_value.place(x=200,y=175)
                # btns
                def back_n_delete(is_del):
                    if is_del == True:
                        del subscriptions[f'subscription_{sub_id}']
                    clear_show_sub()
                    five()
                btn_of_back=Button(window,text='Back',padx=5,pady=5,command=lambda:back_n_delete(False))
                btn_of_back.place(x=110,y=220)

                def edit(sub_id):
                    clear_show_sub()
                    sub_id_label=Label(window,text="sub Id :",font=('sans serifs',14))
                    sub_id_label.place(x=80,y=50)
                    sub_id_entry=Entry(window,width=20)
                    sub_id_entry.insert(0,subscriptions[f'subscription_{sub_id}'].sub_id)
                    sub_id_entry.place(x=160,y=55)
                    temp_idk = sub_id_entry.get()

                    date_label=Label(window,text="date :",font=('sans serifs',14))
                    date_label.place(x=80,y=80)
                    date_entry=Entry(window,width=20)
                    date_entry.insert(0,subscriptions[f'subscription_{sub_id}'].date)
                    date_entry.place(x=160,y=85)

                    customer_id_label=Label(window,text="customer Id :",font=('sans serifs',14))
                    customer_id_label.place(x=80,y=110)
                    customer_id_entry=Entry(window,width=20)
                    customer_id_entry.insert(0,subscriptions[f'subscription_{sub_id}'].cost_id)
                    customer_id_entry.place(x=210,y=115)

                    trainer_id_label=Label(window,text="trainer Id :",font=('sans serifs',14))
                    trainer_id_label.place(x=80,y=140)
                    trainer_id_entry=Entry(window,width=20)
                    trainer_id_entry.insert(0,subscriptions[f'subscription_{sub_id}'].trainer_id)
                    trainer_id_entry.place(x=180,y=145)

                    exersice_id_label=Label(window,text="exersice id :",font=('sans serifs',14))
                    exersice_id_label.place(x=80,y=170)
                    exersice_id_entry=Entry(window,width=20)
                    exersice_id_entry.insert(0,subscriptions[f'subscription_{sub_id}'].exe_id)
                    exersice_id_entry.place(x=200,y=175)

                    # btns
                    def save_n_back(is_save):
                        if is_save == True:
                            del subscriptions[f'subscription_{sub_id}']
                            subscriptions[f'subscription_{int(sub_id_entry.get())}'] = subscription(int(sub_id_entry.get()),date_entry.get(),customer_id_entry.get(),trainer_id_entry.get(),exersice_id_entry.get())

                        sub_id_label.destroy()
                        sub_id_entry.destroy()
                        date_label.destroy()
                        date_entry.destroy()
                        customer_id_label.destroy()
                        customer_id_entry.destroy()
                        trainer_id_label.destroy()
                        trainer_id_entry.destroy()
                        exersice_id_label.destroy()
                        exersice_id_entry.destroy()
                        btn_of_back.destroy()
                        btn_of_save.destroy()
                        show_sub(temp_idk)
                    btn_of_back=Button(window,text='Back',padx=5,pady=5,command=lambda: save_n_back(False))
                    btn_of_back.place(x=110,y=220)
                    btn_of_save=Button(window,text='Save',padx=5,pady=5,command=lambda: save_n_back(True))
                    btn_of_save.place(x=230,y=220)

                btn_of_edit=Button(window,text='edit',padx=5,pady=5,command=lambda: edit(sub_id))
                btn_of_edit.place(x=180,y=220)
                btn_del=Button(window,text='Delete',padx=5,pady=5,command=lambda:back_n_delete(True))
                btn_del.place(x=250,y=220)

        btn_show=Button(window,text='Show',command=lambda:show_sub(sub_id_in_five_entry.get()))
        btn_show.place(x=150,y=85)
        def add_sub():
            clear_five()
            sub_id_label=Label(window,text="sub Id :",font=('sans serifs',14))
            sub_id_label.place(x=80,y=50)
            sub_id_entry=Entry(window,width=20)
            sub_id_entry.place(x=160,y=55)
            date_label=Label(window,text="date :",font=('sans serifs',14))
            date_label.place(x=80,y=80)
            date_entry=Entry(window,width=20)
            date_entry.place(x=160,y=85)
            customer_id_label=Label(window,text="customer Id :",font=('sans serifs',14))
            customer_id_label.place(x=80,y=110)
            customer_id_entry=Entry(window,width=20)
            customer_id_entry.place(x=210,y=115)
            trainer_id_label=Label(window,text="trainer Id :",font=('sans serifs',14))
            trainer_id_label.place(x=80,y=140)
            trainer_id_entry=Entry(window,width=20)
            trainer_id_entry.place(x=180,y=145)
            exersice_id_label=Label(window,text="exersice id :",font=('sans serifs',14))
            exersice_id_label.place(x=80,y=170)
            exersice_id_entry=Entry(window,width=20)
            exersice_id_entry.place(x=200,y=175)

            # btns
            def add_n_back(is_add):
                if is_add == True and f'costumer_{customer_id_entry.get()}' in costumers.keys() and f'trainer_{trainer_id_entry.get()}' in trainers.keys() and f'plan_{exersice_id_entry.get()}' in plans.keys():
                    subscriptions[f'subscription_{int(sub_id_entry.get())}'] = subscription(int(sub_id_entry.get()),date_entry.get(),customer_id_entry.get(),trainer_id_entry.get(),exersice_id_entry.get())
                sub_id_entry.destroy()
                sub_id_label.destroy()
                date_entry.destroy()
                date_label.destroy()
                customer_id_entry.destroy()
                customer_id_label.destroy()
                trainer_id_entry.destroy()
                trainer_id_label.destroy()
                exersice_id_entry.destroy()
                exersice_id_label.destroy()
                btn_of_back.destroy()
                btn_of_add.destroy()
                five()

            btn_of_back=Button(window,text='Back',padx=5,pady=5,command=lambda: add_n_back(False))
            btn_of_back.place(x=110,y=220)
            btn_of_add=Button(window,text='Add',padx=5,pady=5,command=lambda: add_n_back(True))
            btn_of_add.place(x=230,y=220)

        btn_add=Button(window,text='Add new',command=add_sub)
        btn_add.place(x=150,y=120)

        def back():
            clear_five()
            home()
        btn_back=Button(window,text='Back',command=back)
        btn_back.place(x=150,y=150)
        btn_exit=Button(window,text='exit',command=window.quit)
        btn_exit.place(x=150,y=180)

    btn_of_memberships=Button(window,text="Memberships",command=five)
    btn_of_memberships.pack(pady=20,ipadx=5,ipady=5)
    btn_of_exit=Button(window,text="Quit",command=window.quit)
    btn_of_exit.pack(ipadx=10,ipady=5)
home()
window.mainloop()