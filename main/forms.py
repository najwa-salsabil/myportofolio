from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput

from main.models import Project, Experience, Achievement

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Associate of Business Growth and Partnership RISTEK",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi Pengalaman",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = [
            "title",
            "rank",
            "year",
            "description",
        ]

        labels = {
            "title": "Nama/Kompetisi",
            "rank": "Juara/Peran",
            "year": "Tahun",
            "description": "Deskripsi (opsional)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Impact Innovator League",
                    "maxlength": 255,
                }
            ),
            "rank": TextInput(
                attrs={
                    "placeholder": "Finalis",
                }
            ),
            "year": NumberInput(
                attrs={
                    "placeholder": "2026",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi Pencapaian",
                    "rows": 3,
                }
            ),
        }