import time
from pages.base_page import BasePage
from playwright.sync_api import expect

class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.MAIN_LOGO_ABRA = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/a')
        self.SEARCH_FIELD = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[1]/input')
        self.LOGIN_HEADER_ACTIONS = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]')
        self.ALL_CATEGORIES_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[1]/button')
        self.LAST_NEWS_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[2]/ul/li[1]/a')
        self.TUTORIAL_FOR_BUYERS_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[2]/ul/li[2]/a')
        self.SELL_ON_ABRA_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[2]/ul/li[3]/a')
        self.CONTACT_SUPPORT_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[2]/ul/li[4]/a')
        self.FAQ_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[2]/ul/li[5]/a')
        self.ABOUT_US_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[2]/ul/li[6]/a')
        self.CHANGE_LANGUAGE_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[3]/div/div[1]/div/div')
        self.CHANGE_LOCATION_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[2]/div[3]/div/div[2]/div/div')
        self.MAIN_IMAGE = self.page.locator('//*[@id="root"]/div/div/main/div/div[1]/div[1]/div/img')
        self.FIRST_BLOCK_IMAGE = self.page.locator('//*[@id="root"]/div/div/main/div/div[1]/div[2]/div/div[1]/div/img')
        self.SECOND_BLOCK_IMAGE = self.page.locator('//*[@id="root"]/div/div/main/div/div[1]/div[2]/div/div[2]/div/img')
        self.THIRD_BLOCK_IMAGE = self.page.locator('//*[@id="root"]/div/div/main/div/div[1]/div[2]/div/div[3]/div/img')
        self.FOURTH_BLOCK_IMAGE = self.page.locator('//*[@id="root"]/div/div/main/div/div[1]/div[2]/div/div[4]/div/img')
        self.NEW_ARRIVALS_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[2]/div/div[1]/button')
        self.HIGHEST_RATING_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[2]/div/div[2]/button')
        self.HOT_DEALS_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[2]/div/div[3]/button')

        self.CLOTHES_CATEGORY_BLOCK = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[1]')
        self.CLOTHES_CATEGORY_RIGHT_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[1]/div[1]/div[2]/button[2]/svg')
        self.CLOTHES_CATEGORY_LEFT_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[1]/div[1]/div[2]/button[1]/svg')
        self.CLOTHES_CATEGORY_VIEW_MORE_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[1]/div[2]/div/div[23]/div/a')

        self.KIDS_CATEGORY_BLOCK = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[2]')
        self.KIDS_CATEGORY_RIGHT_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[2]/div[1]/div[2]/button[2]/svg')
        self.KIDS_CATEGORY_LEFT_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[2]/div[1]/div[2]/button[1]/svg')
        self.KIDS_CATEGORY_VIEW_MORE_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[1]/div[2]/div[2]/div/div[26]/div/a')

        self.TITLE_EMAIL_MAILING = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[1]/h2')
        self.ENTER_EMAIL_FIELD = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[1]/div/div/input')
        self.SUBSCRIBE_BUTTON = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[1]/div/button')

        self.CONTACT_US_TITLE = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[2]/div[1]/h3')
        self.PHONE_NUMBER = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[2]/div[1]/a/span')

        self.SOCIAL_MEDIA_LINKS_TITLE = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[2]/div[2]/div/h3')
        self.TELEGRAM_LINK = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[2]/div[2]/div/ul/li[1]/a')
        self.INSTAGRAM_LINK = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[2]/div[2]/div/ul/li[2]/a')
        self.VK_LINK = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[2]/div[2]/div/ul/li[3]/a')
        self.GOOGLE_LINK = self.page.locator('//*[@id="root"]/div/div/main/div/div[4]/div/div[2]/div[2]/div/ul/li[4]/a')

        self.BOTTOM_ABRA_LOGO = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/a')
        self.BOTTOM_LAST_NEWS_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[1]/ul/li[1]/a')
        self.BOTTOM_CONTACT_SUPPORT_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[1]/ul/li[4]/a')
        self.BOTTOM_TUTORIAL_FOR_BUYERS_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[1]/ul/li[2]/a')
        self.BOTTOM_FAQ_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[1]/ul/li[5]/a')
        self.BOTTOM_SELL_ON_ABRA_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[1]/ul/li[3]/a')
        self.BOTTOM_ABOUT_US_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[1]/ul/li[6]/a')
        self.BOTTOM_CHANGE_LANGUAGE_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[2]/div/div[1]/div/div')
        self.BOTTOM_CHANGE_LOCATION_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[1]/div[2]/div/div[2]/div/div')

        self.ABRA_COPYRIGHT = self.page.locator('//*[@id="root"]/div/div/footer/div[2]/div/p')
        self.TERMS_AND_CONDITIONS_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[2]/div/a[1]')
        self.PRIVACY_POLICY_BUTTON = self.page.locator('//*[@id="root"]/div/div/footer/div[2]/div/a[2]')
        self.QUESTION_WINDOW = self.page.locator('//*[@id="root"]/div/div/main/div/div[3]/div[2]/a')


    def search_main_logo(self):
        expect(self.MAIN_LOGO_ABRA).to_be_visible()

    def search_searching_field(self):
        expect(self.SEARCH_FIELD).to_be_visible()

    def search_login_header_actions(self):
        expect(self.LOGIN_HEADER_ACTIONS).to_be_visible()

    def search_all_categories_button(self):
        expect(self.ALL_CATEGORIES_BUTTON).to_be_visible()

    def search_last_news_button(self):
        expect(self.LAST_NEWS_BUTTON).to_be_visible()

    def search_tutorial_for_buyers_button(self):
        expect(self.TUTORIAL_FOR_BUYERS_BUTTON).to_be_visible()

    def search_sell_on_abra_button(self):
        expect(self.SELL_ON_ABRA_BUTTON).to_be_visible()

    def search_contact_support_button(self):
        expect(self.CONTACT_SUPPORT_BUTTON).to_be_visible()

    def search_faq_button(self):
        expect(self.FAQ_BUTTON).to_be_visible()

    def search_about_us_button(self):
        expect(self.ABOUT_US_BUTTON).to_be_visible()

    def search_change_language_button(self):
        expect(self.CHANGE_LANGUAGE_BUTTON).to_be_visible()

    def search_change_location_button(self):
        expect(self.CHANGE_LOCATION_BUTTON).to_be_visible()

    def search_main_image(self):
        expect(self.MAIN_IMAGE).to_be_visible()

    def search_first_block_image(self):
        expect(self.FIRST_BLOCK_IMAGE).to_be_visible()

    def search_second_block_image(self):
        expect(self.SECOND_BLOCK_IMAGE).to_be_visible()

    def search_third_block_image(self):
        expect(self.THIRD_BLOCK_IMAGE).to_be_visible()

    def search_fourth_block_image(self):
        expect(self.FOURTH_BLOCK_IMAGE).to_be_visible()

    def search_new_arrivals_button(self):
        expect(self.NEW_ARRIVALS_BUTTON).to_be_visible()

    def search_highest_rating_button(self):
        expect(self.HIGHEST_RATING_BUTTON).to_be_visible()

    def search_hot_deals_button(self):
        expect(self.HOT_DEALS_BUTTON).to_be_visible()

    def search_clothes_category_block(self):
        expect(self.CLOTHES_CATEGORY_BLOCK).to_be_visible()

    def search_clothes_category_right_button(self):
        expect(self.CLOTHES_CATEGORY_RIGHT_BUTTON).to_be_visible()

    def search_clothes_category_left_button(self):
        expect(self.CLOTHES_CATEGORY_LEFT_BUTTON).to_be_visible()

    def search_clothes_category_view_more_button(self):
        expect(self.CLOTHES_CATEGORY_VIEW_MORE_BUTTON).to_be_visible()

    def search_kids_category_block(self):
        expect(self.KIDS_CATEGORY_BLOCK).to_be_visible()

    def search_kids_category_right_button(self):
        expect(self.KIDS_CATEGORY_RIGHT_BUTTON).to_be_visible()

    def search_kids_category_left_button(self):
        expect(self.KIDS_CATEGORY_LEFT_BUTTON).to_be_visible()

    def search_kids_category_view_more_button(self):
        expect(self.KIDS_CATEGORY_VIEW_MORE_BUTTON).to_be_visible()

    def search_title_email_mailing(self):
        expect(self.TITLE_EMAIL_MAILING).to_be_visible()

    def search_enter_email_field(self):
        expect(self.ENTER_EMAIL_FIELD).to_be_visible()

    def search_subscribe_button(self):
        expect(self.SUBSCRIBE_BUTTON).to_be_visible()

    def search_contact_us_title(self):
        expect(self.CONTACT_US_TITLE).to_be_visible()

    def search_phone_number(self):
        expect(self.PHONE_NUMBER).to_be_visible()

    def search_social_media_links_title(self):
        expect(self.SOCIAL_MEDIA_LINKS_TITLE).to_be_visible()

    def search_telegram_link(self):
        expect(self.TELEGRAM_LINK).to_be_visible()

    def search_instagram_link(self):
        expect(self.INSTAGRAM_LINK).to_be_visible()

    def search_vk_link(self):
        expect(self.VK_LINK).to_be_visible()

    def search_google_link(self):
        expect(self.GOOGLE_LINK).to_be_visible()

    def search_bottom_abra_logo(self):
        expect(self.BOTTOM_ABRA_LOGO).to_be_visible()

    def search_bottom_last_news_button(self):
        expect(self.BOTTOM_LAST_NEWS_BUTTON).to_be_visible()

    def search_bottom_contact_support_button(self):
        expect(self.BOTTOM_CONTACT_SUPPORT_BUTTON).to_be_visible()

    def search_bottom_tutorial_for_buyers_button(self):
        expect(self.BOTTOM_TUTORIAL_FOR_BUYERS_BUTTON).to_be_visible()

    def search_bottom_faq_button(self):
        expect(self.BOTTOM_FAQ_BUTTON).to_be_visible()

    def search_bottom_sell_on_abra_button(self):
        expect(self.BOTTOM_SELL_ON_ABRA_BUTTON).to_be_visible()

    def search_bottom_about_us_button(self):
        expect(self.BOTTOM_ABOUT_US_BUTTON).to_be_visible()

    def search_bottom_change_language_button(self):
        expect(self.BOTTOM_CHANGE_LANGUAGE_BUTTON).to_be_visible()

    def search_bottom_change_location_button(self):
        expect(self.BOTTOM_CHANGE_LOCATION_BUTTON).to_be_visible()

    def search_abra_copyright(self):
        expect(self.ABRA_COPYRIGHT).to_be_visible()

    def search_terms_and_conditions_button(self):
        expect(self.TERMS_AND_CONDITIONS_BUTTON).to_be_visible()

    def search_privacy_policy_button(self):
        expect(self.PRIVACY_POLICY_BUTTON).to_be_visible()

    def search_question_window(self):
        expect(self.QUESTION_WINDOW).to_be_visible()


