# IoT

Presentation for IoT

## Content

Trong link này mình all info. [Info](https://github.com/microsoft/IoT-For-Beginners/tree/main/2-farm/lessons/4-migrate-your-plant-to-the-cloud)

Sau khi hỏi lại thầy thì mình cứ đăng nhập Azure Free, xong rồi demo cho mọi người biết thôi.

Mình có các mục nội dung:

1. Introduction
2. Tóm tắt phần trước đã học (vì mình là nhóm đầu tiên của tuần, tui nghĩ là mình nên kiểu dẫn dắt)

> _✅ Do you think this would allow companies to move quickly? If an online clothing retailer suddenly got popular due to a celebrity being seen in their clothes, would they be able to increase their computing power quickly enough to support the sudden influx of orders?_

Đây sẽ là một câu hỏi dẫn dắt để vô Cloud

3. Giới thiệu về Cloud

- Sustainability (trong phần note nhỏ).
- Giới thiệu 1 số cloud service (Azure, AWS, Google Cloud)
   > _Một cái tính theo tiếng, một cái tính theo phút._
- Tập trung vào Azure và phần mình sẽ sử dụng trong presentation.

4. Tạo Azure subscription

- Giới thiệu Azure Student
- Giới thiệu Azure Free

5. Cloud Services

- Concerns với public broker.
- Research về 
  > _✅ Do some research: What is the downside of having an open IoT service where any device or code can connect? Can you find specific examples of hackers taking advantage of this?_
- IoT Hub

6. Use Azure CLI

- Create resource group
- Create IoT Hub
  > regions: giới thiệu + chọn region.

7. Communicate with IoT Hub

- Protocol: MQTT, AMQP, HTTP
- Research
  > _✅ Do some research: Read more on these message types on the Device-to-cloud communications guidance, and the Cloud-to-device communications guidance in the IoT Hub documentation._

8. Connect device to cloud

- này là demo --> có gì mình bàn kỹ hơn.

9. Trả lời cái challenge cuối cùng.

    🚀 Challenge  

    The free tier of IoT Hub allows 8,000 messages a day. The code you wrote sends telemetry messages every 10 seconds. How many messages a day is one message every 10 seconds?

    Think about how often soil moisture measurements should be sent? How can you change your code to stay within the free tier and check as often as needed but not too often? What if you wanted to add a second device?

    > Cái này là tui trả lời rồi nên có gì mình bàn sau nhé.

10. Bàn về Cloud Service

  - IaaS, PaaS, SaaS, serverless


# Task list

Phú: 3 4 5 7 10 (SaaS serverless)  
Dương: 1 2 6 8 9 10 (IaaS PaaS)

# Todo:

- [ ] 1. Introduction
- [ ] 2. Tóm tắt phần trước đã học
- [ ] 3. Giới thiệu về Cloud
- [ ] 4. Tạo Azure subscription
- [ ] 5. Cloud Services
- [ ] 6. Use Azure CLI
- [ ] 7. Communicate with IoT Hub
- [ ] 8. Connect device to cloud
- [ ] 9. Trả lời cái challenge cuối cùng.
- [ ] 10. Bàn về Cloud Service

