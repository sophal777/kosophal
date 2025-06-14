import os
import random
import string
import os
import zipfile
import requests
import shutil
import subprocess

import phonenumbers
import random
import string
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
import requests

def get_browser_version(browser):
    browser = browser.lower()
    if browser == "chrome":
        return get_chrome_version()
    elif browser == "edge":
        return get_edge_version()
    else:
        return None


def get_chrome_version():
    try:
        result = subprocess.run(
            ['reg', 'query', r'HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon', '/v', 'version'],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, shell=True
        )
        if result.returncode != 0 or "version" not in result.stdout.lower():
            raise Exception("Chrome not found in registry")
        version_line = result.stdout.strip().split('\n')[-1]
        version = version_line.split()[-1]
        return version
    except Exception:
        return None


def get_edge_version():
    try:
        result = subprocess.run(
            ['reg', 'query', r'HKEY_CURRENT_USER\Software\Microsoft\Edge\BLBeacon', '/v', 'version'],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, shell=True
        )
        if result.returncode != 0 or "version" not in result.stdout.lower():
            raise Exception("Edge not found in registry")
        version_line = result.stdout.strip().split('\n')[-1]
        version = version_line.split()[-1]
        return version
    except Exception:
        return None


def download_Chrome(version):
    try:
        version_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
        json_data = requests.get(version_url).json()
        full_version = json_data['channels']['Stable']['version']
        base_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{full_version}/win32/chromedriver-win32.zip"
        return base_url
    except Exception:
        return None


def download_Edge(version):
    try:
        base_url = f"https://msedgedriver.azureedge.net/{version}/edgedriver_win32.zip"
        return base_url
    except Exception:
        return None


def KH_driver(browser="chrome", folder="webdriver"):
    browser = browser.lower()
    driver_path = os.path.join(folder, f"{browser}driver.exe")

    if os.path.exists(driver_path):
        return driver_path

    browser_version = get_browser_version(browser)
    if not browser_version:
        return None

    if browser == "chrome":
        url = download_Chrome(browser_version)
    elif browser == "edge":
        url = download_Edge(browser_version)
    else:
        return None

    if not url:
        return None

    response = requests.get(url, stream=True)
    if response.status_code != 200:
        return None

    os.makedirs(folder, exist_ok=True)
    zip_path = os.path.join(folder, f"{browser}driver.zip")

    with open(zip_path, "wb") as file:
        file.write(response.content)

    if not zipfile.is_zipfile(zip_path):
        return None

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(folder)

    extracted_driver_path = None
    for root, dirs, files in os.walk(folder):
        for file in files:
            if f"{browser}driver.exe" in file.lower():
                extracted_driver_path = os.path.join(root, file)
                break

    if not extracted_driver_path:
        return None

    shutil.move(extracted_driver_path, driver_path)
    os.remove(zip_path)

    return driver_path
def installer():

    KH = KH_driver("chrome")
    KH=KH_driver("edge")


def generate_valid_phone_number(country="phone_kh", valid_numbers=1, NAME="nonosophal", APP_MIL="yandex", number=5, foun=3):
    def generate_email():
        raw_number = ''.join(random.choices(string.digits, k=number))
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(foun))
        email = f"{NAME}{raw_number}{random_string}@{APP_MIL}.com"
        return email

    def validate_and_return(phone_str, region):
        try:
            parsed = phonenumbers.parse(phone_str, region)
            if phonenumbers.is_valid_number(parsed):
                return phone_str
            return None
        except NumberParseException:
            return None

    if country == "email" or country in ["yahoo", "yandex", "gmail"]:
        return generate_email()

    valid_phone_list = []
    while len(valid_phone_list) < valid_numbers:
        if country == "phone_kh":
            prefixes = ['+85596', '+85597', '+85588', '+85571']
            phone = random.choice(prefixes) + str(random.randint(1000000, 9999999))
            valid_phone = validate_and_return(phone, "KH")
        elif country == "phone_us":
            phone = '+1' + str(random.randint(2000000000, 9999999999))
            valid_phone = validate_and_return(phone, "US")
        elif country == "phone_th":
            phone = '+66' + str(random.randint(100000000, 999999999))
            valid_phone = validate_and_return(phone, "TH")
        elif country == "phone_vn":
            phone = '+84' + str(random.randint(100000000, 999999999))
            valid_phone = validate_and_return(phone, "VN")
        elif country == "phone_jp":
            phone = '+81' + str(random.randint(100000000, 999999999))
            valid_phone = validate_and_return(phone, "JP")
        else:
            print("Country not supported.")
            return None
        if valid_phone:
            valid_phone_list.append(valid_phone)
    return valid_phone_list if valid_numbers > 1 else valid_phone_list[0]



def generate_random_name(language="Khmer"):
    name_data = {
        "Khmer": ([
            'សុភា', 'ចាន់ដា', 'រ័ត្ន', 'ស្រីពៅ', 'វិច្ឆិកា', 'សុខា', 'ធារី', 'រ៉ានី',
            'ភារម្យ', 'សំណាង', 'វិសាល', 'គន្ធា', 'រ៉ាវុធ', 'សុជាតិ', 'នារី', 'ផានិត',
            'គីមហួន', 'សុភាព', 'ម៉ានី', 'រ៉ាស៊ី', 'ធីណា', 'សុភី', 'ស៊ីណា', 'ភាព',
            'វណ្ណា', 'ប៊ុនថា', 'សុភ័ណ្ឌ', 'រ៉ាវី', 'គឹមលី', 'សុខភី', 'នីតា', 'ផល្លី',
            'សុភ័ក្ត្រ', 'រ៉ាម៉ា', 'គន្ធី', 'សុភ័ត', 'វិរៈ', 'សុភ័ន', 'រ៉ាវ័ន្ត', 'គឹមសាន',
            'សុខនា', 'ភារថ', 'នីរ៉ា', 'សុភ័ស', 'រ៉ាវ៉ាន', 'គន្ធារី', 'សុខរ៉ា', 'ផល្លា',
            'វណ្ណី', 'សុភ័ន្ត', 'រ៉ាសុខ', 'គឹមរ៉ា', 'សុខលី', 'ភាវី', 'នីរ៉ាន', 'ផលសុខ',
            'សុភ័ក្តិ', 'រ៉ាវ៉ា', 'គន្ធាន', 'សុខភា', 'វិរ៉ា', 'សុភ័ណ', 'រ៉ាវ័ត', 'គឹមភា',
            'សុខនី', 'ភារី', 'នីរ៉ាស', 'សុភ័រ', 'រ៉ាវ៉ាន្ត', 'គន្ធារ៉ា', 'សុខរ៉ាន', 'ផល្លាន',
            'វណ្ណ៉ា', 'សុភ័ន្តា', 'រ៉ាសុខា', 'គឹមរ៉ាន', 'សុខលា', 'ភាវ៉ា', 'នីរ៉ាត', 'សុភ័ស្ត',
            'រ៉ាវ៉ាត', 'គន្ធារ៉ាន'
        ], [
            'ឈឿន', 'សោម', 'សុខ', 'ជាតិ', 'អ៊ុន', 'ហ៊ុន', 'លី', 'គឹម',
            'ចាន់', 'ថន', 'គង់', 'សេង', 'ឯម', 'ខន', 'អ៊ុយ', 'ផល',
            'ម៉ៅ', 'ហេង', 'ឈី', 'អន', 'ភួន', 'សុន', 'កែវ', 'ឡា',
            'គួច', 'ធា', 'សុភា', 'រ៉ា', 'គន្ធ', 'វ៉ាន', 'ភល', 'សុខា',
            'នី', 'ឈឿនា', 'សោមា', 'ជាតា', 'អ៊ុនា', 'ហ៊ុនា', 'លីន', 'គឹមា',
            'ចានា', 'ថនា', 'គង់ា', 'សេងា', 'ឯមា', 'ខនា', 'អ៊ុយា', 'ផលា',
            'ម៉ៅា', 'ហេងា', 'ឈីន', 'អនា', 'ភួនា', 'សុនា', 'កែវា', 'ឡាន',
            'គួចា', 'ធាន', 'សុភាន', 'រ៉ាន', 'គន្ធា', 'វ៉ានា', 'ភលា', 'សុខាន',
            'នីន', 'ឈឿនី', 'សោមី', 'ជាតី', 'អ៊ុនី', 'ហ៊ុនី', 'លីណា', 'គឹមី',
            'ចានី', 'ថនី', 'គង់ី', 'សេងី', 'ឯមី', 'ខនី', 'អ៊ុយី', 'ផលី',
            'ម៉ៅី', 'ហេងី'
        ]),
        "Thai": ([
            'ชัย', 'พันธ์', 'ลิ้ม', 'จันทร์', 'ศรี', 'วงศ์', 'บุญ', 'ทอง',
            'สุข', 'แก้ว', 'มี', 'ขันธ์', 'ยศ', 'ใจ', 'ดี', 'พงษ์',
            'ศักดิ์', 'จิต', 'น้อย', 'ใหญ่', 'คำ', 'เทศ', 'พิมพ์', 'ศิริ',
            'รัก', 'แสง', 'พรม', 'ยง', 'จัน', 'สี', 'ทรัพย์', 'ไชย',
            'สุวรรณ', 'จิตต์', 'ขาว', 'ดำ', 'แดง', 'เขียว', 'เหลือง', 'น้ำ',
            'ปาน', 'วงค์', 'หงษ์', 'ทิพย์', 'ศรีเมือง', 'ชื่น', 'พูน', 'ไพศาล',
            'สุขสันต์', 'จันทร', 'พิมล', 'ศรีสุข', 'รุ่ง', 'ทองดี', 'ไชยยศ', 'ประเสริฐ',
            'สุวรรณดี', 'จิตราพงศ์', 'ขยัน', 'ดีงาม', 'แสงทอง', 'พงษ์ศักดิ์', 'ศรีจันทร์', 'รักดี',
            'ทองคำ', 'จันทร์ดี', 'พิมพ์ศรี', 'ศิริชัย', 'รุ่งเรือง', 'ทองสุข', 'ไชยวัฒน์', 'ประสงค์',
            'สุวรรณศรี', 'จิตรดี', 'ขยันดี', 'ดีใจ', 'แสงศรี', 'พงษ์ทอง', 'ศรีประไพ', 'รักศรี'
        ], [
            'สมชาย', 'สุดา', 'นิรันดร์', 'อนงค์', 'กิตติ', 'วรรณี', 'ชัยวัฒน์', 'สุรี',
            'ธนา', 'จิรา', 'วรุต', 'นภา', 'ศักดิ์', 'กานต์', 'ภัทร', 'วีรา',
            'สุนทร', 'มานะ', 'รัตน์', 'นารี', 'ชัย', 'ศรี', 'ธานี', 'ประภา',
            'วิทวัส', 'สมศักดิ์', 'จันทร์', 'วรพจน์', 'สุนีย์', 'ก้อง', 'ภัทราวดี', 'ชัยยศ',
            'สุวรรณ', 'มนัส', 'รัตนา', 'นฤมล', 'ชัยมงคล', 'ศรีวรรณ', 'ธนกฤต', 'ประไพ',
            'วิชัย', 'สมจิตร', 'จิรวรรณ', 'วรัญญา', 'สุนทรี', 'กิตติพงษ์', 'ภัทรวดี', 'ชัยภัทร',
            'สุวลี', 'มนต์ชัย', 'รัตติกาล', 'นลินี', 'ชัยรัตน์', 'ศรีสุดา', 'ธนวัฒน์', 'ประภาส',
            'วิมล', 'สมบัติ', 'จิรพงษ์', 'วรางค์', 'สุนันท์', 'กิตติชัย', 'ภัทริน', 'ชัยวุฒิ',
            'สุวลักษณ์', 'มนต์', 'รัตน์มณี', 'นพมาศ', 'ชัยยงค์', 'ศรีสมร', 'ธนชัย', 'ประพจน์',
            'วิศรุต', 'สมยศ', 'จิรนันท์', 'วรวิทย์', 'สุนทราพร', 'กิตติศักดิ์', 'ภัทรพงศ์', 'ชัยวัฒน์'
        ]),
        "English": ([
            'John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah', 'David', 'Laura',
            'James', 'Emma', 'William', 'Olivia', 'Thomas', 'Sophia', 'Robert', 'Isabella',
            'Daniel', 'Ava', 'Joseph', 'Mia', 'Charles', 'Charlotte', 'Henry', 'Amelia',
            'George', 'Elizabeth', 'Benjamin', 'Harper', 'Samuel', 'Evelyn', 'Jack', 'Abigail',
            'Matthew', 'Sofia', 'Andrew', 'Ella', 'Christopher', 'Grace', 'Ryan', 'Lily',
            'Nicholas', 'Victoria', 'Nathan', 'Chloe', 'Jonathan', 'Hannah', 'Steven', 'Zoe',
            'Richard', 'Avery', 'Edward', 'Aria', 'Paul', 'Addison', 'Mark', 'Aubrey',
            'Kevin', 'Layla', 'Brian', 'Kayla', 'Eric', 'Savannah', 'Scott', 'Brooklyn',
            'Patrick', 'Ellie', 'Jason', 'Lillian', 'Justin', 'Samantha', 'Timothy', 'Claire',
            'Gregory', 'Hazel', 'Jeffrey', 'Madeline', 'Frank', 'Scarlett', 'Gary', 'Eleanor',
            'Dennis', 'Nora', 'Bruce', 'Eden'
        ], [
            'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson', 'Davis', 'Clark', 'Harris',
            'Lewis', 'Walker', 'Hall', 'Allen', 'Young', 'King', 'Wright', 'Scott',
            'Green', 'Adams', 'Baker', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts',
            'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart',
            'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy',
            'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres',
            'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders',
            'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins',
            'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler',
            'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz',
            'Hayes', 'Myers', 'Ford', 'Hamilton'
        ]),
        "Vietnamese": ([
            'Anh', 'Hương', 'Nam', 'Linh', 'Dũng', 'Mai', 'Thảo', 'Phong',
            'Hùng', 'Lan', 'Tuấn', 'Ngọc', 'Bình', 'Thanh', 'Khoa', 'Phương',
            'Đức', 'Hà', 'Việt', 'Yến', 'Quân', 'Hạnh', 'Tâm', 'Cường',
            'Thu', 'Minh', 'Hải', 'Trang', 'An', 'Khánh', 'Hòa', 'Thắng',
            'Ngân', 'Long', 'Hiệp', 'Nhi', 'Quang', 'Mai', 'Huy', 'Thư',
            'Đạt', 'Nhung', 'Tùng', 'Ly', 'Vinh', 'Thúy', 'Kiên', 'Hằng',
            'Sơn', 'Phúc', 'Nga', 'Trí', 'Bích', 'Khôi', 'Oanh', 'Hoàng',
            'Nhật', 'Lan', 'Thành', 'Tuyến', 'Hảo', 'My', 'Công', 'Hiền',
            'Duy', 'Thùy', 'Hiếu', 'Liễu', 'Quý', 'Thảo', 'Trung', 'Hương',
            'Tín', 'Loan', 'Vũ', 'Nhiên', 'Khang', 'Phượng', 'Toàn', 'Thắm',
            'Châu', 'Diệu', 'Bảo', 'Hồng'
        ], [
            'Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Vũ', 'Đặng', 'Bùi',
            'Đỗ', 'Hồ', 'Ngô', 'Dương', 'Lý', 'Vương', 'Trương', 'Đinh',
            'Phan', 'Mai', 'Tô', 'Đào', 'Tăng', 'Quách', 'Lương', 'Văn',
            'Bạch', 'Lưu', 'Đoàn', 'Hà', 'Tạ', 'Bùi', 'Giang', 'Châu',
            'La', 'Triệu', 'Trịnh', 'Lâm', 'Phùng', 'Nông', 'Âu', 'Cao',
            'Đàm', 'Hồng', 'Khúc', 'Tôn', 'Vi', 'Mạc', 'Kiều', 'Khổng',
            'Hứa', 'Doãn', 'Hàn', 'Nghiêm', 'Quyền', 'Tăng', 'Điền', 'Bế',
            'Lã', 'Lục', 'Ninh', 'Đồng', 'Thái', 'Hùng', 'Võ', 'Hình',
            'Bàng', 'Tần', 'Hà', 'Âu Dương', 'Lăng', 'Thẩm', 'Tào', 'Cung',
            'Đường', 'Phí', 'Tống', 'Đại', 'Hạ', 'Trần', 'Mạch', 'Nhan',
            'Vạn', 'Diệp', 'Hồ', 'Khưu'
        ]),
        "Japanese": ([
            'Hiroshi', 'Yuki', 'Aiko', 'Ken', 'Sakura', 'Taro', 'Mika', 'Ryo',
            'Haruka', 'Daichi', 'Ayaka', 'Kenta', 'Sora', 'Yuna', 'Takumi', 'Mai',
            'Shota', 'Hana', 'Riku', 'Asuka', 'Kaito', 'Mio', 'Yuto', 'Rina',
            'Ren', 'Aoi', 'Hiro', 'Nana', 'Tetsuya', 'Miu', 'Soma', 'Hinata',
            'Akira', 'Mina', 'Sho', 'Nozomi', 'Ryota', 'Yui', 'Daiki', 'Ami',
            'Tsubasa', 'Mei', 'Haruto', 'Kanako', 'Yuma', 'Saki', 'Ryoma', 'Emi',
            'Kota', 'Kaede', 'Sota', 'Moe', 'Taichi', 'Mizuki', 'Rui', 'Hikaru',
            'Yusuke', 'Ayano', 'Shunya', 'Risa', 'Hayato', 'Mana', 'Takanori', 'Yume',
            'Kosei', 'Chihiro', 'Arata', 'Saori', 'Tomoya', 'Nao', 'Koki', 'Eri',
            'Shoma', 'Asahi', 'Takuya', 'Maki', 'Ryusei', 'Kana', 'Hiroki', 'Misaki',
            'Soma', 'Yuka', 'Tatsuya', 'Kokoa'
        ], [
            'Tanaka', 'Yamamoto', 'Sato', 'Suzuki', 'Takahashi', 'Nakamura', 'Kobayashi', 'Kato',
            'Ito', 'Watanabe', 'Yamada', 'Sasaki', 'Yamaguchi', 'Matsumoto', 'Inoue', 'Kimura',
            'Hayashi', 'Saito', 'Shimizu', 'Yamazaki', 'Mori', 'Abe', 'Ikeda', 'Hashimoto',
            'Ishii', 'Ishikawa', 'Nakajima', 'Maeda', 'Fujita', 'Ogawa', 'Okada', 'Goto',
            'Hasegawa', 'Murakami', 'Kondo', 'Ishida', 'Ueda', 'Morioka', 'Ota', 'Kaneko',
            'Fujii', 'Saito', 'Endo', 'Aoki', 'Fujiwara', 'Nishimura', 'Fukuda', 'Miura',
            'Nakagawa', 'Okamoto', 'Matsuda', 'Harada', 'Ono', 'Tamura', 'Takeuchi', 'Kaneda',
            'Nakano', 'Hara', 'Shibata', 'Sakamoto', 'Miyazaki', 'Kikuchi', 'Yokoyama', 'Imamura',
            'Nishioka', 'Ueno', 'Maruyama', 'Kawamura', 'Otsuka', 'Imai', 'Sano', 'Kojima',
            'Miyamoto', 'Kubo', 'Toyoda', 'Sakai', 'Kawasaki', 'Inada', 'Uemura', 'Sugiyama',
            'Komatsu', 'Nitta', 'Oshima', 'Kawaguchi'
        ]),
        "Korean": ([
            'Ji-hoon', 'Min-ji', 'Seo-yun', 'Tae-hyung', 'Soo-jin', 'Min-seo', 'Joon-ho', 'Ha-eun',
            'Dong-hyun', 'Ji-won', 'Seo-jin', 'Tae-young', 'Min-ho', 'Eun-ji', 'Joon-woo', 'Ha-rin',
            'Hyun-woo', 'Ji-yeon', 'Seo-hyun', 'Tae-min', 'Soo-hyun', 'Min-jung', 'Joon-young', 'Ha-young',
            'Jae-hyun', 'Ji-soo', 'Seo-yeon', 'Tae-woo', 'Soo-yeon', 'Min-jae', 'Joon-sung', 'Ha-jin',
            'Hyun-jun', 'Ji-hye', 'Seo-jun', 'Tae-jun', 'Soo-yeon', 'Min-soo', 'Joon-hyuk', 'Ha-neul',
            'Jae-min', 'Ji-min', 'Seo-woo', 'Tae-soo', 'Soo-jung', 'Min-kyu', 'Joon-hee', 'Ha-ram',
            'Hyun-soo', 'Ji-eun', 'Seo-hyeon', 'Tae-hyun', 'Soo-kyung', 'Min-seok', 'Joon-jae', 'Ha-joon',
            'Jae-woo', 'Ji-young', 'Seo-hoon', 'Tae-kyung', 'Soo-bin', 'Min-chul', 'Joon-kyu', 'Ha-min',
            'Hyun-jin', 'Ji-hyun', 'Seo-young', 'Tae-ho', 'Soo-mi', 'Min-woo', 'Joon-ho', 'Ha-yoon'
        ], [
            'Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Kang', 'Cho', 'Yoon',
            'Jang', 'Lim', 'Han', 'Oh', 'Seo', 'Shin', 'Kwon', 'Hwang',
            'Ahn', 'Song', 'Ryu', 'Hong', 'Jeon', 'Moon', 'Yang', 'Bae',
            'Baek', 'Heo', 'Noh', 'Nam', 'Sim', 'Gwak', 'Sung', 'Yu',
            'Yoo', 'Jo', 'Jeong', 'Goo', 'Koh', 'Ma', 'Chun', 'Do',
            'Chang', 'Son', 'Hyeon', 'Byun', 'Yeom', 'Yum', 'Won', 'Kong',
            'Hwan', 'Meng', 'Bang', 'Kyung', 'Pyo', 'Gong', 'Bok', 'Ham',
            'Ye', 'Yeo', 'Chu', 'Joo', 'Hah', 'Ha', 'Cheon', 'Pan',
            'Eom', 'Uhm', 'Cha', 'Jin', 'Min', 'Boo', 'Pi', 'Pyo',
            'Seok', 'Suk', 'Hye', 'Hae', 'On', 'Ok', 'Woo', 'Wee',
            'Wi', 'Hwa', 'Huo', 'Ho'
        ])
    }
    first_names, last_names = name_data.get(language, (["NoName"], ["NoName"]))
    return random.choice(first_names), random.choice(last_names)

def random_birthday():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1970, 2005)
    return f"{month:02d}/{day:02d}/{year}"

def random_password(length=10):
    symbols = ['@', '#', '$', '%']
    rand_part = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    symbol = random.choice(symbols)
    number = str(random.randint(100, 999))
    return f"{symbol}{rand_part}{symbol}{number}"

def random_gender():
    return random.choice(["Male", "Female"])

def random_all():
    bday = random_birthday()
    gen = random_gender()
    pwd = random_password()
    phone_number = generate_valid_phone_number("phone_kh")
    gmail = generate_valid_phone_number("email", NAME="nonosophal", APP_MIL="gmail")
    first_name, last_name = generate_random_name("Khmer")
    
    data = f"{first_name}|{last_name}|{bday}|{gen}|{phone_number}|{pwd}|{gmail}"
    return data



def download_images():
    os.makedirs("icons", exist_ok=True)
    url = "https://api.github.com/repos/sophal777/icons_png/contents"
    try:
        imgs = requests.get(url).json()
    except Exception as e:
        print(f"[!] Error fetching image list: {e}")
        return

    for img in imgs:
        if img['name'].endswith('.png'):
            path = os.path.join("icons", img['name'])
            if os.path.exists(path):
                print(f"Skip {img['name']} (already exists)")
                continue
            try:
                r = requests.get(img['download_url'])
                r.raise_for_status()
                with open(path, "wb") as f:
                    f.write(r.content)
                print(f"Downloaded {img['name']}")
            except Exception as e:
                print(f"[!] Error downloading {img['name']}: {e}")
