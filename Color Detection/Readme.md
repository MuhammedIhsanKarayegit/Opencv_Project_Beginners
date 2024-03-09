This project is a simple beginner level project that I made to improve myself in OpenCv.
If we come to the purpose of the project, it is a simple detection project that determines what color an image given as a path from the outside is.
If we look at the construction stages of the project, first we get the path of the image whose color we want to find from the user and find_color into the function named function. The working principle of the function we use is to first convert the received image into HSV color space and then find the color of the image given by the user by determining which of the predetermined color boundaries this image belongs to with if - else conditions.

------------------------------------------------------------------------------------------------------------------------------------------

Bu proje OpenCv'de kendimi geliştirmek için yaptığım başlangıç seviyesinde basit bir projedir.
Projenin amacına gelecek olursak dışarıdan yol olarak verilen bir görüntünün hangi renk olduğunu belirleyen basit bir algılama projesidir.
Projenin yapım aşamalarına bakacak olursak ilk olarak kullanıcıdan rengini bulmak istediğimiz resmin yolunu alıyoruz ve find_color 
isimli fonksiyonun içine yerleştiriyoruz. Kullandığımız fonksiyonun çalışma prensibi, alınan görüntüyü önce HSV renk uzayına çevirmek ve daha sonra bu görüntünün önceden belirlenmiş renk sınırlarından hangisine ait olduğunu if - else koşulları ile belirleyerek kullanıcı tarafından verilen görüntünün rengini bulmaktır.
