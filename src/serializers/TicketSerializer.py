from rest_framework import serializers
from ..models import Ticket, SoldTicket


class SoldTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldTicket
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    soldTicket = SoldTicketSerializer(
        source="soldticket_set", many=True, read_only=True
    )

    class Meta:
        model = Ticket
        fields = "__all__"
