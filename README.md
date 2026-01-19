# AAS-703-Kendali-Robotika
BT_Robot

Behavior Tree (BT) Robot TurtleBot3 dengan ROS2 Humble

Deskripsi

bt_robot adalah package ROS2 berbasis Python untuk mengendalikan robot TurtleBot3 menggunakan logika Behavior Tree sederhana.
Robot dapat maju saat jalan kosong dan berbelok ketika mendeteksi obstacle menggunakan sensor LIDAR.

Program ini dijalankan di simulator Gazebo dan menggunakan sensor LIDAR untuk mendeteksi jarak di depan robot.

Fitur

Sensor LIDAR mendeteksi obstacle di depan.

Robot maju jika jalan aman.

Robot berbelok saat ada obstacle.

Logika Behavior Tree sederhana untuk kontrol gerak robot.

Kesimpulan

Robot dapat bergerak dan sensor LIDAR mendeteksi obstacle.

Namun, robot belum bisa menghindari obstacle dengan baik, kadang tetap menabrak atau terbalik.

Untuk pengembangan selanjutnya, disarankan:

Menambahkan deteksi obstacle samping.

Mengatur kecepatan linear dan angular proporsional.

Menambahkan strategi belok lebih cerdas.
