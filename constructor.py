import json


class ManageData:
    jumlah = 0
    Waktu = []
    Senin = []
    Selasa = []
    Rabu = []
    Kamis = []
    Jumat = []
    Sabtu = ["Tidak Ada"]

    def __init__(self):
        data_ = open("data.json")
        data = json.loads(data_.read())
        # print(type(data))
        # print(data)
        # print(data["app"][1]['hari'])
        for d in range(1):
            Waktu = data["Waktu"]
            self.Waktu = Waktu
            Senin = data["Senin"]
            self.Senin = Senin
            Selasa = data["Selasa"]
            self.Selasa = Selasa
            Rabu = data["Rabu"]
            self.Rabu = Rabu
            Kamis = data["Kamis"]
            self.Kamis = Kamis
            Jumat = data["Jumat"]
            self.Jumat = Jumat
            if data["Sabtu"]["ada"] == True:
                Sabtu = data["Sabtu"]['isi']
                self.Sabtu = Sabtu
            else:
                pass
        data_.close()
        # print(self.Senin)
        # print(self.Selasa)
        # return Senin, Selasa, Rabu, Kamis, Jumat

    # def insertData(self, x):
    #     insert = {
    #         "hari": x,
    #     }
    #     data_ = open("data.json")
    #     data = json.loads(data_.write())
    #     data.append(insert)
    #     data_.seek(0)
    #     json.dumps(data, data_)
    #     data_.close()

    # def readData(self):
    #     data_ = open("data.json")
    #     data = json.loads(data_.read())
    #     # print(type(data))
    #     # print(data)
    #     # print(data["app"][1]['hari'])
    #     for d in range(1):
    #         Senin = data["Senin"]
    #         self.Senin = Senin
    #         Selasa = data["Selasa"]
    #         self.Selasa = Selasa
    #         Rabu = data["Rabu"]
    #         self.Rabu = Rabu
    #         Kamis = data["Kamis"]
    #         self.Kamis = Kamis
    #         Jumat = data["Jumat"]
    #         self.Jumat = Jumat
    #         if data["Sabtu"]["ada"] == True:
    #             Sabtu = data["Sabtu"]['isi']
    #             self.Sabtu = Sabtu
    #         else:
    #             pass
    #     data_.close()
    #     print(self.Senin)
    #     print(self.Selasa)
    #     return Senin, Selasa, Rabu, Kamis, Jumat


# d = ManageData()
# print(d.Jumat)
