Chào, mình là Huỳnh Ngọc Thắng, đến từ HCMUTE - Đại học Sư phạm Kỹ thuật TP.HCM.

Dự án này được lấy cảm hứng từ AL FATH TERRY: https://www.kaggle.com/code/alfathterry/american-sign-language-real-time-detection.
Bạn có thể tham khảo cách xây dựng bản demo cơ bản tại liên kết trên.
Ngoài ra, mình cũng đã tham khảo thêm nhiều dự án trên Kaggle và lấy dataset từ đây: https://www.kaggle.com/competitions/asl-fingerspelling/discussion/409443.
Liên hệ nếu có câu hỏi: https://web.facebook.com/profile.php?id=100016660993579
Cảm ơn đến Computer vision enginner: https://www.youtube.com/watch?v=MJCSjXepaAM đã giúp mình học cách sử dụng Scikit, Mediapipe và OpenCV.
Dự án của mình đang được thử nghiệm trên kênh YouTube: https://www.youtube.com/@ticasslo.

Từ đó, mình đã thêm một số tính năng như sau:
- Thu thập dữ liệu (Cảm ơn  Computer vision enginne: https://www.youtube.com/watch?v=MJCSjXepaAM).
- Phát hiện mô hình.
- Tạo giao diện GUI cho từng tính năng. Dùng thư viện customtinkler
- Chuyển đổi ngôn ngữ ký hiệu ASL thành giọng nói hoặc văn bản
- Tạo một trò chơi dựa trên tính năng ASL thành giọng nói
- Tạo một chế độ học tập/hình ảnh hóa để mọi người có thể dễ dàng học cơ bản về ASL.


Bắt đầu nhé:
Tại sao không làm VSL (ngôn ngữ ký hiệu Việt Nam)?
Vì nó rất khó để thực hiện. Một số từ và ký tự cần đến chuyển động để nhận dạng.
Nhưng dự án này chỉ tập trung vào nhận diện tĩnh, không phải chuyển động.
Ngoài ra, Việt Nam có 3 loại ký hiệu từ Bắc đến Nam, và mình không thể tìm được dataset phù hợp cho VSL, nên dự án chủ yếu tập trung vào ASL.

Dataset của ASL được lấy từ Kaggle. có dữ liệu sẵn thì sẽ dễ dùng hơn
Không làm number, vì rất dễ nhầm lẫn.

Như mình đã nói, ASL có 2 cũng có ký tự cần chuyển động là J và Z. Nhưng trong dự án này, mình sẽ làm dạng tĩnh cho J và Z.
Có sự khác biệt về các biến thể của ký tự như: M, N, T. Nhưng mình chỉ sử dụng một biến thể từ dataset.


Đọc từ file collect_imgs.py -> data_extraction -> model_training -> real_time_prediction/AI. Bạn có thể hiểu các câu hỏi như
OpenCV là gì, Mediapipe là gì, Scikit-learn/ Random forest là gì
Tại sao cần data_extraction?
Tại sao sử dụng AI?
Làm sao để phát hiện kí tự?
Tại sao dùng threading?.....













Hi im Huỳnh Ngọc Thắng from HCMUTE - Ho Chi Minh University of Technology and Education

The project is inspired from AL FATH TERRY  https://www.kaggle.com/code/alfathterry/american-sign-language-real-time-detection
You can check the basic of how the demo is created there
check more project from kaggle, i also get my dataset here: https://www.kaggle.com/competitions/asl-fingerspelling/discussion/409443

Credit to Computer vision engineer https://www.youtube.com/watch?v=MJCSjXepaAM to help me learn how Scikit and Mediapipe, openCV work

Im testing/showing my project on my youtube https://www.youtube.com/@ticasslo
Contact me if there any question: https://web.facebook.com/profile.php?id=100016660993579

From there i have add in feature such as:
1. How to collect data? (Credit to Computer vision engineer https://www.youtube.com/watch?v=MJCSjXepaAM)
2. How to detect model?
3. Make a GUI for each feature. I used customtinkler for it
4. Make an ASL into Voice/Text feature
5. Create a ASL game base on the ASL into Voice
6. Create a learn/visualization so people can basic read on ASL

Now let get started:
- The problem i didnt do VSL: Vietnamese sign language is because it very hard to do. Some word and character need movement to identify
but this is just a simple detection base on STATIC not moving. And because vietnam have 3 type of sign from North to South
Also i cant find a dataset for VSL so main go is ASL
Dataset of ASL is from kaggle
- No number here cause it really easy to mess up
- As i said ASL do have 2 moving character is J and Z. But we are going simple so just do a static J and Z
- There is different sign/varient of character like: M, N, T. But we gonna go with one from the dataset

- Read from collect_imgs.py -> data_extraction -> model_training -> real_time_prediction/ AI
+ Why need data data_extraction? Why use AI? How to detect? ..... Why threading?















