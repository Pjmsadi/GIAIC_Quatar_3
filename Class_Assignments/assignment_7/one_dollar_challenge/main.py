import streamlit as st
from io import StringIO

class ProfileCardApp:
    def __init__(self):
        st.set_page_config(page_title="My Profile Card", page_icon="👤", layout="centered")
        self.set_background()
        self.name = ""
        self.bio = ""
        self.email = ""
        self.social = ""
        self.skills = []
        self.uploaded_file = None

    def set_background(self):
        st.markdown("""
            <style>
                body {
                    background-color: #f3e8ff;
                }
                .stApp {
                    background-color: #f3e8ff;
                }
                .stTextInput > div > div > input {
                    background-color: #fff;
                    border-radius: 8px;
                }
                .stTextArea textarea {
                    background-color: #fff;
                    border-radius: 8px;
                }
            </style>
        """, unsafe_allow_html=True)

    def show_title(self):
        st.title("👤 My Profile Card")
        st.write("Create a beautiful personal profile in seconds!")

    def get_user_input(self):
        with st.form("profile_form"):
            self.name = st.text_input("👤 Your Name")
            self.bio = st.text_area("🧠 About You", placeholder="Share a short bio...")
            self.email = st.text_input("📧 Email")
            self.social = st.text_input("🔗 LinkedIn / GitHub / Portfolio URL")
            skills_input = st.text_input("💼 Skills (comma-separated)", placeholder="Python, Streamlit, AI")
            self.skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]
            self.uploaded_file = st.file_uploader("📸 Upload Profile Picture", type=["jpg", "png"])
            submitted = st.form_submit_button("✨ Generate My Card")
        return submitted

    def display_profile(self):
        st.divider()
        st.subheader("🎉 Your Profile Card")

        with st.container():
            col1, col2 = st.columns([1, 2])

            with col1:
                if self.uploaded_file:
                    st.image(self.uploaded_file, width=200, caption=self.name)
                else:
                    st.warning("No profile image uploaded.")

            with col2:
                st.markdown(f"### {self.name}")
                st.markdown(f"**📧 Email:** {self.email}")
                st.markdown(f"**🔗 Social:** {self.social}")
                st.info(self.bio)

                if self.skills:
                    st.markdown("#### 💼 Skills")
                    st.markdown(", ".join([f"`{skill}`" for skill in self.skills]))

        st.divider()

        if st.button("📁 Download Profile Summary"):
            profile_text = self.generate_profile_text()
            st.download_button(
                label="Download as Text File",
                data=profile_text,
                file_name=f"{self.name.replace(' ', '_')}_profile.txt",
                mime="text/plain"
            )

    def generate_profile_text(self):
        text = f"""Name: {self.name}
Email: {self.email}
Social: {self.social}

Bio:
{self.bio}

Skills:
{', '.join(self.skills)}
"""
        return text

    def run(self):
        self.show_title()
        if self.get_user_input():
            self.display_profile()


# Run the app
if __name__ == "__main__":
    app = ProfileCardApp()
    app.run()
