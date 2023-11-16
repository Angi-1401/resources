from django.db import models
from django.utils.translation import gettext_lazy as _


class ResourceOrigin(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Resource Origins")

    def __str__(self):
        return self.name


class ResourceCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Resource Categories")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, verbose_name=_("Last Name"))
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name=_("Date of Birth")
    )
    date_of_death = models.DateField(
        null=True, blank=True, verbose_name=_("Date of Death")
    )

    class Meta:
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Entity(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Entities")

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Collections")

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Faculties")

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _("Schools")

    def __str__(self):
        return self.name


class Career(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _("Careers")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Subjetcs")

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _("Themes")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Languages")

    def __str__(self):
        return self.name


class License(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField()

    class Meta:
        verbose_name_plural = _("Licenses")

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Keywords")

    def __str__(self):
        return self.name


class Format(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Formats")

    def __str__(self):
        return self.name


class Resource(models.Model):
    resource_category = models.ForeignKey(
        ResourceCategory, on_delete=models.CASCADE, verbose_name=_("Resource Category")
    )
    resource_origin = models.ForeignKey(
        ResourceOrigin, on_delete=models.CASCADE, verbose_name=_("Resource Origin")
    )
    international_id = models.CharField(
        max_length=255, verbose_name=_("International ID")
    )
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, verbose_name=_("Author"))
    publish_date = models.DateField(verbose_name=_("Publish Date"))
    coverage_start = models.DateField(
        null=True, blank=True, verbose_name=_("Coverage (Start)")
    )
    coverage_end = models.DateField(
        null=True, blank=True, verbose_name=_("Coverage (End)")
    )
    entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE, verbose_name=_("Entity")
    )
    edition = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Edition")
    )
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, verbose_name=_("Collection")
    )
    career = models.ManyToManyField(Career, verbose_name=_("Career"))
    theme = models.ManyToManyField(Theme, verbose_name=_("Theme"))
    language = models.ManyToManyField(Language, verbose_name=_("Language"))
    license = models.ForeignKey(
        License, on_delete=models.CASCADE, verbose_name=_("License")
    )
    abstract = models.TextField(verbose_name=_("Abstract"))
    url = models.URLField(null=True, blank=True, verbose_name=_("URL"))
    location = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=_("Location")
    )
    adquisition_date = models.DateField(
        null=True, blank=True, verbose_name=_("Adquisition Date")
    )
    keyword = models.ManyToManyField(Keyword, verbose_name=_("Keyword"))
    format = models.ManyToManyField(Format, verbose_name=_("Format"))

    class Meta:
        verbose_name_plural = _("Resources")

    def __str__(self):
        return self.title
