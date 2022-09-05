from rest_framework import serializers
from ..models import SoldTicket, Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class SoldTicketSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(many=False, read_only=True)

    class Meta:
        model = SoldTicket
        fields = "__all__"
