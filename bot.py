from dotenv import load_dotenv
import os
import requests
import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def start(update, context):
    welcome_message = ("Selamat Datang di Chatbot Layanan Informasi Kerja Praktek dan Tugas Akhir Program Studi Teknik Informatika Universitas Semarang.\n\n"
                       "Pilih Informasi yang ingin Anda cari:")

    options = [['💼 Kerja Praktek'], ['🎓 Tugas Akhir']]

    reply_markup = ReplyKeyboardMarkup(options, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(welcome_message, reply_markup=reply_markup)

def kerja_praktek(update, context):
    global kp_options, kp_reply_markup
    kp_options = [['Syarat KP', 'Biaya KP'], ['Prosedur Administrasi KP', 'Koordinator KP'], ['Bidang Magang KP', 'Pengajuan Judul KP'],['Bimbingan KP','Pengerjaan Laporan KP'], ['Lainnya']]
    kp_reply_markup = ReplyKeyboardMarkup(kp_options, one_time_keyboard=True, resize_keyboard=True)
    context.user_data['info_type'] = 'KP'
    update.message.reply_text("Pilih Informasi Kerja Praktek yang ingin Anda cari:", reply_markup=kp_reply_markup)

def tugas_akhir(update, context):
    ta_options = [['Syarat TA', 'Biaya TA'], ['Topik TA', 'Koordinator TA'], ['Penilaian TA', 'Pengajuan Judul TA'], ['Bimbingan TA', 'Penulisan Proposal & Laporan TA'], ['Lainnya']]
    ta_reply_markup = ReplyKeyboardMarkup(ta_options, one_time_keyboard=True, resize_keyboard=True)
    context.user_data['info_type'] = 'TA'
    update.message.reply_text("Pilih Informasi Tugas Akhir yang ingin Anda cari:", reply_markup=ta_reply_markup)


def handle_message(update, context):
    user_text = update.message.text
    if user_text == '💼 Kerja Praktek':
        context.user_data['info_type'] = 'KP'
        kp_options = [['Syarat KP', 'Biaya KP'], ['Prosedur Administrasi KP', 'Koordinator KP'], ['Bidang Magang KP', 'Pengajuan Judul KP'],['Bimbingan KP','Pengerjaan Laporan KP'], ['Lainnya']]
        kp_reply_markup = ReplyKeyboardMarkup(kp_options, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text("Pilih Informasi Kerja Praktek yang ingin Anda cari:", reply_markup=kp_reply_markup)
    elif user_text == 'Bidang Magang KP':
        back_option = [['Kembali']]
        back_reply_markup = ReplyKeyboardMarkup(back_option, one_time_keyboard=True, resize_keyboard=True)
        context.user_data['info_type'] = 'KP'
        update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/kp-ta-usm.appspot.com/o/pekerjaan-materi-kp.png?alt=media&token=25ddc4e6-aaa3-446c-9bbc-1dffbbed2b9c", caption="Diatas merupakan Tabel Pekerjaan dan Materi Magang yang bisa Anda gunakan sebagai acuan dalam melaksanakan Kerja Praktek.", reply_markup=back_reply_markup)
    elif user_text == 'Pengajuan Judul KP':
        back_option = [['Kembali']]
        back_reply_markup = ReplyKeyboardMarkup(back_option, one_time_keyboard=True, resize_keyboard=True)
        context.user_data['info_type'] = 'KP'
        update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/kp-ta-usm.appspot.com/o/alur-kp.png?alt=media&token=fe52dfa4-2452-43f3-9c96-98a7b3423d8f", caption="Diatas merupakan Alur Pengajuan Judul Kerja Praktek.\nPastikan untuk menghubungi Koordinator atau Dosen Pembimbing setelah melakukan pengajuan di SIMA agar segera dikonfirmasi dan divalidasi.\n\nUntuk Alur Pengajuan Judul Kerja Praktek di SIMA bisa Anda akses melalui link berikut:\nhttps://drive.google.com/file/d/1YX6RIIUIUPhwSqSm7Q36p16iweVLNt59/view?usp=sharing", reply_markup=back_reply_markup)
    elif user_text == 'Bimbingan KP':
        back_option = [['Kembali']]
        back_reply_markup = ReplyKeyboardMarkup(back_option, one_time_keyboard=True, resize_keyboard=True)
        context.user_data['info_type'] = 'KP'
        update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/kp-ta-usm.appspot.com/o/Alur%20Bimbingan%20Laporan%20KP.jpg?alt=media&token=f56aedb2-3b34-4084-ab80-640878423171", caption="Diatas merupakan Alur Bimbingan Kerja Praktek di SIMA.\nPastikan untuk menghubungi Dosen Pembimbing setelah melakukan pengajuan bimbingan di SIMA agar segera dikonfirmasi dan dikoreksi.\nLakukan Bimibingan 5 kali agar bisa lanjut ke tahap Seminar/Ujian KP.", reply_markup=back_reply_markup)
    elif user_text == 'Revisi Laporan KP':
        back_option = [['Kembali']]
        back_reply_markup = ReplyKeyboardMarkup(back_option, one_time_keyboard=True, resize_keyboard=True)
        context.user_data['info_type'] = 'KP'
        update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/kp-ta-usm.appspot.com/o/Alur%20Revisi%20Laporan%20KP%20di%20SIMA.png?alt=media&token=e7b9f46b-ff70-4e3d-9dc5-f1087fedf6b0", caption="Diatas merupakan Alur Revisi Laporan Kerja Praktek di SIMA.\nRevisi laporan maksimal 1 minggu dari tanggal seminar dan dikumpulkan maksimal 1 minggu setelah ACC revisi.", reply_markup=back_reply_markup)
    elif user_text == 'Konversi MBKM & PKM':
        back_option = [['Kembali']]
        back_reply_markup = ReplyKeyboardMarkup(back_option, one_time_keyboard=True, resize_keyboard=True)
        context.user_data['info_type'] = 'KP'
        update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/kp-ta-usm.appspot.com/o/Konversi%20MBKM%20%26%20PKM-KP.jpg?alt=media&token=b2eab428-4320-433c-ae12-e7b85f4b94cf", caption="Diatas merupakan Alur Konversi MBKM dan PKM untuk Kerja Praktek.\nTopik/Konsentrasi Kerja Praktek sesuai dengan Proyek Akhir yang dikerjakan pada MBKM atau PKM.\nKonversi MBKM dan PKM dilakukan setelah melakukan Seminar/Ujian Kerja Prakterk.", reply_markup=back_reply_markup)
    elif user_text == '🎓 Tugas Akhir':
        context.user_data['info_type'] = 'TA'
        ta_options = [['Syarat TA', 'Biaya TA'], ['Topik TA', 'Koordinator TA'], ['Penilaian TA', 'Pengajuan Judul TA'], ['Bimbingan TA', 'Penulisan Proposal & Laporan TA'], ['Lainnya']]
        ta_reply_markup = ReplyKeyboardMarkup(ta_options, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text("Pilih Informasi Tugas Akhir yang ingin Anda cari:", reply_markup=ta_reply_markup)
    elif user_text == 'Topik TA':
        back_option = [['Kembali']]
        back_reply_markup = ReplyKeyboardMarkup(back_option, one_time_keyboard=True, resize_keyboard=True)
        context.user_data['info_type'] = 'TA'
        update.message.reply_photo("https://firebasestorage.googleapis.com/v0/b/kp-ta-usm.appspot.com/o/Topik%20Tugas%20Akhir.png?alt=media&token=40576932-3be1-45c3-9815-143dcbf06f41", caption="Diatas merupakan Tabel Topik Tugas Akhir yang bisa Anda ambil sesuai minat dan kemampuan Anda.", reply_markup=back_reply_markup)
    elif user_text == 'Lainnya' or user_text == 'Kembali':
        info_type = context.user_data.get('info_type')
        if info_type == 'KP' and user_text == 'Lainnya':
            kp_options_more = [['Penulisan Laporan KP', 'Lampiran KP'], ['Syarat Seminar KP', 'Daftar Seminar KP'], ['Tata Cara Seminar KP', 'Syarat Pakaian Seminar KP'], ['Revisi Laporan KP', 'Penyerahan Berkas KP'], ['Penilaian KP','Konversi MBKM & PKM'], ['Kembali']]
            kp_reply_markup_more = ReplyKeyboardMarkup(kp_options_more, one_time_keyboard=True, resize_keyboard=True)
            update.message.reply_text("Pilih Informasi Kerja Praktek Lainnya yang ingin Anda cari:", reply_markup=kp_reply_markup_more)
        elif info_type == 'TA' and user_text == 'Lainnya':
            ta_options_more = [['Lampiran TA', 'Daftar Sidang & Revisi TA'], ['Tata Cara Sidang TA', 'Syarat Pakaian Sidang TA'], ['Penyerahan Berkas TA'], ['Kembali']]
            ta_reply_markup_more = ReplyKeyboardMarkup(ta_options_more, one_time_keyboard=True, resize_keyboard=True)
            update.message.reply_text("Pilih Informasi Tugas Akhir Lainnya yang ingin Anda cari:", reply_markup=ta_reply_markup_more)
        elif user_text == 'Kembali':
            info_type = context.user_data.get('info_type')
            if info_type == 'KP':
                kp_options = [['Syarat KP', 'Biaya KP'], ['Prosedur Administrasi KP', 'Koordinator KP'], ['Bidang Magang KP', 'Pengajuan Judul KP'], ['Bimbingan KP', 'Pengerjaan Laporan KP'], ['Lainnya']]
                kp_reply_markup = ReplyKeyboardMarkup(kp_options, one_time_keyboard=True, resize_keyboard=True)
                update.message.reply_text("Pilih Informasi Kerja Praktek yang ingin Anda cari:", reply_markup=kp_reply_markup)
            elif info_type == 'TA':
                ta_options = [['Syarat TA', 'Biaya TA'], ['Topik TA', 'Koordinator TA'], ['Penilaian TA', 'Pengajuan Judul TA'], ['Bimbingan TA', 'Penulisan Proposal & Laporan TA'], ['Lainnya']]
                ta_reply_markup = ReplyKeyboardMarkup(ta_options, one_time_keyboard=True, resize_keyboard=True)
                update.message.reply_text("Pilih Informasi Tugas Akhir yang ingin Anda cari:", reply_markup=ta_reply_markup)
    elif update.message.text:
        user_question = update.message.text
        payload = {"question": user_question.lower()}

        headers = {
            "Ocp-Apim-Subscription-Key": os.getenv('API_KEY'),
            "Content-Type": "application/json"
        }

        response = requests.post("https://kp-ta-ti-bot.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=kp-ta-bot&api-version=2021-10-01&deploymentName=production", json=payload, headers=headers)

        if response.status_code == 200:
            answer = response.json()["answers"][0]["answer"]
            if context.user_data.get('info_type') == 'KP':
                back_button = 'Kembali'
            elif context.user_data.get('info_type') == 'TA':
                back_button = 'Kembali'
            option = [[back_button]]
            reply_markup = ReplyKeyboardMarkup(option, one_time_keyboard=True, resize_keyboard=True)
            update.message.reply_text(answer, reply_markup=reply_markup)     
        else:
            update.message.reply_text("Maaf, terjadi kesalahan dalam mengambil informasi. Silakan coba lagi nanti.")
    else:
        # Echo balik pesan yang diterima jika bukan pilihan yang didukung
        update.message.reply_text("Jawaban Tidak Ditemukan.")

# Fungsi utama untuk menjalankan bot
def main():

    # Buat updater untuk bot
    updater = Updater(os.getenv('TOKEN'), use_context=True)

    # Dapatkan dispatcher untuk menangani perintah dan pesan
    dp = updater.dispatcher

    # Daftarkan handler untuk perintah /start
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("kerjapraktek", kerja_praktek))
    dp.add_handler(CommandHandler("tugasakhir", tugas_akhir))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Mulai bot
    updater.start_polling()

    logger.info("Bot started polling...")

    # Biarkan bot berjalan hingga dihentikan secara manual
    updater.idle()

if __name__ == '__main__':
    main()
