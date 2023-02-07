from PIL import Image


im = Image.open("C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Cardgame_Icon.png")
output_path = "C:\\Users\\Jonas\\Documents\\Studium\\Master\\01_VRLab\\Cardgame_Icon\\"

im_1 = im.resize(size=(88, 88), resample=0)

im_2 = im.resize(size=(142, 142), resample=0)

im_3 = im.resize(size=(300, 300), resample=0)

im_4 = im.resize(size=(620, 620), resample=2)
im_4 = im_4.convert("RGB")

im_5 = im.resize(size=(100, 100), resample=0)

im_6 = im.resize(size=(24, 24), resample=0)

im_7 = im.resize(size=(50, 50), resample=0)

im_8 = im.resize(size=(1240, 600), resample=0)
im_8 = im_8.convert("RGB")

im_9 = im.resize(size=(620, 300), resample=0)

im_1.save(output_path + "88x88.png")
im_2.save(output_path + "142x142.png")
im_3.save(output_path + "300x300.png")
im_4.save(output_path + "620x620.jpg", optimize=True, quality=95)
im_5.save(output_path + "100x100.png")
im_6.save(output_path + "24x24.png")
im_7.save(output_path + "50x50.png")
im_8.save(output_path + "1240x600.jpg", optimize=True, quality=95)
im_9.save(output_path + "620x300.png")
