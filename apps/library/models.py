import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from languages.fields import LanguageField


# Create your models here.
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        max_length=255,
        verbose_name=_("First Name"),
        help_text=_("The first name of the author."),
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_("Last Name"),
        help_text=_("The last name of the author."),
    )

    class Meta:
        verbose_name_plural = _("Authors")

    def __str__(self):
        initials = "".join([name[0].upper() + "." for name in self.first_name.split()])
        return self.last_name + ", " + initials


class Clasification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the classification."),
    )

    class Meta:
        verbose_name_plural = _("Resource Categories")

    def __str__(self):
        return self.name


class Repository(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the repository."),
    )

    class Meta:
        verbose_name = _("Repository")
        verbose_name_plural = _("Repositories")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the Publisher."),
    )

    class Meta:
        verbose_name_plural = _("Publishers")

    def __str__(self):
        return self.name


class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the collection."),
    )

    class Meta:
        verbose_name_plural = _("Collections")

    def __str__(self):
        return self.name


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the faculty."),
    )

    class Meta:
        verbose_name_plural = _("Faculties")

    def __str__(self):
        return self.name


class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the school."),
    )
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, verbose_name=_("Faculty")
    )

    class Meta:
        verbose_name_plural = _("Schools")

    def __str__(self):
        return self.name


class Career(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the career."),
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name=_("School")
    )

    class Meta:
        verbose_name_plural = _("Careers")

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the subject."),
    )

    class Meta:
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return self.name


class Theme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the theme."),
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name=_("Subject")
    )

    class Meta:
        verbose_name_plural = _("Themes")

    def __str__(self):
        return self.name


class License(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the license."),
    )
    description = models.TextField(help_text=_("Description of the license."))

    class Meta:
        verbose_name_plural = _("Licenses")

    def __str__(self):
        return self.name


class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the keyword."),
    )

    class Meta:
        verbose_name_plural = _("Keywords")

    def __str__(self):
        return self.name


class Format(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
        help_text=_("The name of the format."),
    )

    class Meta:
        verbose_name_plural = _("Formats")

    def __str__(self):
        return self.name


class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    international_id = models.CharField(
        max_length=255,
        verbose_name=_("International ID"),
        help_text=_("The international ID of the resource."),
    )
    clasification = models.ForeignKey(
        Clasification,
        on_delete=models.CASCADE,
        verbose_name=_("Resource Category"),
        help_text=_("The category of the resource."),
    )
    title = models.CharField(max_length=255, help_text=_("The title of the resource."))
    edition = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Edition"),
        help_text=_("The edition of the resource."),
    )
    author = models.ManyToManyField(Author, verbose_name=_("Author"))
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        verbose_name=_("Publisher"),
        help_text=_("The Publisher associated with the resource."),
    )
    publish_date = models.DateField(
        verbose_name=_("Publish Date"),
        help_text=_("The date when the resource was published."),
    )
    coverage_start = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Coverage (Start)"),
        help_text=_("The start date of the resource coverage."),
    )
    coverage_end = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Coverage (End)"),
        help_text=_("The end date of the resource coverage."),
    )
    extension = models.CharField(
        max_length=255,
        verbose_name=_("Extension"),
        help_text=_("The extension of the resource."),
    )
    language = LanguageField(
        max_length=255,
        verbose_name=_("Language"),
        help_text=_("The language of the resource."),
    )
    license = models.ForeignKey(
        License,
        on_delete=models.CASCADE,
        verbose_name=_("License"),
        help_text=_("The license of the resource."),
    )
    abstract = models.TextField(
        verbose_name=_("Abstract"), help_text=_("A brief summary of the resource.")
    )
    repository = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        verbose_name=_("Repository"),
        help_text=_("The origin of the resource."),
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        verbose_name=_("Collection"),
        help_text=_("The collection associated with the resource."),
    )
    career = models.ManyToManyField(
        Career, verbose_name=_("Career"), help_text=_("The career of the resource.")
    )
    theme = models.ManyToManyField(
        Theme, verbose_name=_("Theme"), help_text=_("The theme of the resource.")
    )
    url = models.URLField(
        null=True,
        blank=True,
        verbose_name=_("URL"),
        help_text=_("The URL of the resource (if apply)."),
    )
    location = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Location"),
        help_text=_("The physical location of the resource (if apply)."),
    )
    adquisition_date = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Acquisition Date"),
        help_text=_("The date when the resource was acquired."),
    )
    keyword = models.ManyToManyField(
        Keyword, verbose_name=_("Keyword"), help_text=_("The keywords of the resource.")
    )
    format = models.ManyToManyField(
        Format, verbose_name=_("Format"), help_text=_("The format of the resource.")
    )

    class Meta:
        verbose_name_plural = _("Resources")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("resource-detail", args=[str(self.id)])
