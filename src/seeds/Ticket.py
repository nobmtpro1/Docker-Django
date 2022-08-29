from ..models import Ticket


def seed():
    Ticket.objects.all().delete()
    Ticket.objects.bulk_create(
        [
            Ticket(
                type="online",
                name="Marketing management",
                date="2022-08-31 12:17:55.000000",
                _from="09:17:55.000000",
                to="12:17:55.000000",
                quantity=200,
                address="146 Bis, đường Nguyễn Văn Thủ, phường Đa Kao, quận 1, TP. HCM",
                price=100000,
                link_video="https://www.youtube.com/embed/WoSigjZrc1Y",
            ),
            Ticket(
                type="offline",
                name="Content creative",
                date="2022-09-12 12:17:55.000000",
                _from="13:17:55.000000",
                to="17:17:55.000000",
                quantity=250,
                address="146 Bis, đường Nguyễn Văn Thủ, phường Đa Kao, quận 1, TP. HCM",
                price=200000,
                link_video="https://www.youtube.com/embed/dvjmauVFlpo",
            ),
        ]
    )
